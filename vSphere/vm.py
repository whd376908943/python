#!/usr/bin/env python
"""
Written by huidong.wang

Clone a VM from template example
"""
from __future__ import with_statement
from pyVmomi import vim, vmodl
from pyVim.connect import SmartConnect, Disconnect, ConnectNoSSL
from pyVim import connect
import atexit
import sys
import re
import time

# 虚拟机创建过程中阻塞


def wait_for_task(task):
    """ wait for a vCenter task to finish """
    task_done = False
    while not task_done:
        if task.info.state == 'success':
            return task.info.result

        if task.info.state == 'error':
            print("there was an error")
            task_done = True
            sys.exit(1)


# 获取单个对象
def get_obj(content, vimtype, name):
    """
    Return an object by name, if name is None the
    first found object is returned
    """
    obj = None
    container = content.viewManager.CreateContainerView(
        content.rootFolder, vimtype, True)
    for c in container.view:
        if name:
            if c.name == name:
                obj = c
                break
        else:
            obj = c
            break
    return obj


def clone_vm(
        content, template, vm_name, si, datastore_name, resource_pool,
        datacenter_name=None, vm_folder=None, cluster_name=None,
        power_on=True, datastorecluster_name=None):

    # if none git the first one
    datacenter = get_obj(content, [vim.Datacenter], datacenter_name)

    if vm_folder:
        destfolder = get_obj(content, [vim.Folder], vm_folder)
    else:
        destfolder = datacenter.vmFolder

    if datastore_name:
        datastore = get_obj(content, [vim.Datastore], datastore_name)
    else:
        datastore = get_obj(
            content, [vim.Datastore], template.datastore[0].info.name)

    # if None, get the first one
    cluster = get_obj(content, [vim.ClusterComputeResource], cluster_name)

    if resource_pool:
        resource_pool = get_obj(content, [vim.ResourcePool], resource_pool)
    else:
        resource_pool = cluster.resourcePool

    vmconf = vim.vm.ConfigSpec()

    if datastorecluster_name:
        podsel = vim.storageDrs.PodSelectionSpec()
        pod = get_obj(content, [vim.StoragePod], datastorecluster_name)
        podsel.storagePod = pod

        storagespec = vim.storageDrs.StoragePlacementSpec()
        storagespec.podSelectionSpec = podsel
        storagespec.type = 'create'
        storagespec.folder = destfolder
        storagespec.resourcePool = resource_pool
        storagespec.configSpec = vmconf

        try:
            rec = content.storageResourceManager.RecommendDatastores(
                storageSpec=storagespec)
            rec_action = rec.recommendations[0].action[0]
            real_datastore_name = rec_action.destination.name
        except():
            real_datastore_name = template.datastore[0].info.name

        datastore = get_obj(content, [vim.Datastore], real_datastore_name)

    # set relospec
    relospec = vim.vm.RelocateSpec()
    relospec.datastore = datastore
    relospec.pool = resource_pool

    clonespec = vim.vm.CloneSpec()
    clonespec.location = relospec
    clonespec.powerOn = power_on

    print("cloning VM...")
    task = template.Clone(folder=destfolder, name=vm_name, spec=clonespec)
    wait_for_task(task)


def vm(args):
    # connect this thing

    si = ConnectNoSSL(
        host=args['host'],
        user=args['user'],
        pwd=args['password'])

    # disconnect this thing
    atexit.register(Disconnect, si)

    content = si.RetrieveContent()
    template = None

    template = get_obj(content, [vim.VirtualMachine], args['template'])

    if template:
        clone_vm(
            content, template, args['vm_name'], si,
            args['datastore_name'],
            args['resource_pool'])
    else:
        print("template not found")

    # 获取新建vm实例的uuid
    vm = get_obj(content, [vim.VirtualMachine], args['vm_name'])
    uuid = vm.config.uuid
    # 初始化vm实例, ip配置
    print('vm 启动中...')
    # 等待30s, 待vmware tools启动
    time.sleep(30)
    print('vm init...')
    args.update(vm_uuid=uuid)
    print('vm ip config...')
    init_vm(args)
    args.update(program_arguments='restart')
    args.update(path_to_program='/etc/init.d/network')
    print('vm network restart')
    init_vm(args)


def init_vm(args):

    try:

        service_instance = connect.SmartConnectNoSSL(host=args['host'],
                                                     user=args['user'],
                                                     pwd=args['password']
                                                     )

        atexit.register(connect.Disconnect, service_instance)
        content = service_instance.RetrieveContent()

        # if instanceUuid is false it will search for VM BIOS UUID instead
        vm = content.searchIndex.FindByUuid(datacenter=None,
                                            uuid=args['vm_uuid'],
                                            vmSearch=True,
                                            instanceUuid=False)

        if not vm:
            raise SystemExit("Unable to locate the virtual machine.")

        tools_status = vm.guest.toolsStatus
        if (tools_status == 'toolsNotInstalled' or
                tools_status == 'toolsNotRunning'):
            raise SystemExit(
                "VMwareTools is either not running or not installed. "
                "Rerun the script after verifying that VMwareTools "
                "is running")

        creds = vim.vm.guest.NamePasswordAuthentication(
            username=args['vm_user'], password=args['vm_pwd']
        )

        try:
            pm = content.guestOperationsManager.processManager

            ps = vim.vm.guest.ProcessManager.ProgramSpec(
                programPath=args['path_to_program'],
                arguments=args['program_arguments']
            )
            res = pm.StartProgramInGuest(vm, creds, ps)

            if res > 0:
                print("Program submitted, PID is %d" % res)
                pid_exitcode = pm.ListProcessesInGuest(vm, creds,
                                                       [res]).pop().exitCode
                # If its not a numeric result code, it says None on submit
                while (re.match('[^0-9]+', str(pid_exitcode))):
                    print("Program running, PID is %d" % res)
                    time.sleep(5)
                    pid_exitcode = pm.ListProcessesInGuest(vm, creds,
                                                           [res]).pop().\
                        exitCode
                    if (pid_exitcode == 0):
                        print("Program %d completed with success" % res)
                        break
                    # Look for non-zero code to fail
                    elif (re.match('[1-9]+', str(pid_exitcode))):
                        print("ERROR: Program %d completed with Failute" % res)
                        print("  tip: Try running this on guest  to debug")
                        print("ERROR: More info on process")
                        print(pm.ListProcessesInGuest(vm, creds, [res]))
                        break

        except(IOError, e):
            print(e)
    except(vmodl.MethodFault) as error:
        print("Caught vmodl fault : " + error.msg)
        return -1

    return 0


def init(args):
    vm(args)

