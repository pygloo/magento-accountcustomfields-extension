# python import
import os, shutil, stat, sys, tarfile, time

# PERMISSION
CHMOD = stat.S_IRWXU | stat.S_IRGRP | stat.S_IWGRP
UID = 1000 # 33
GID = 1000 # 33

def _path(path, uid, gid):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    # change rights
    os.chown(path, uid, gid)
    os.chmod(path, int(CHMOD))
    # useful
    return path

# PATHS
MAGENTO_PATH = '/home/florent/Dev/Src/Php/sites/hexotol' # os.path.join('/srv', 'http', 'nginx', 'dummy_1_5')
BACKUP_PATH = _path(os.path.join('..', 'backup'), 1000, 1000)

# EXTENSION NAME
EXT_NAME = 'magento-imageswitcher-extension'

# prepare backup extension path
BCK_EXT_PATH = _path(
        os.path.join(BACKUP_PATH, EXT_NAME),
        1000, 1000)

# prepare push/pull flag
INSTALL = sys.argv[1] == 'install'
REMOVE = sys.argv[1] == 'remove'
SYNC = sys.argv[1] == 'sync'


def _copy_rights(src, dst, uid, gid):
    # do copy
    shutil.copy(src, dst)
    # change rights
    os.chown(dst, uid, gid)
    os.chmod(dst, int(CHMOD))


def _update_path(path):
    for _p, dirs, files in os.walk(path):
        if _p.startswith('.git'):
            continue
        else:
            # prepare paths
            if INSTALL is True:
                _uid = UID
                _gid = GID
            else:
                _uid = 1000
                _gid = 1000
            # init clean flag
            _to_clean = False
            # ensure destination paths
            _dst_dir = _path(os.path.join(MAGENTO_PATH, _p), _uid, _gid)
            _bck_dir = _path(os.path.join(BCK_EXT_PATH, _p), 1000, 1000)
            # push files
            for _f in files:
                if _f.endswith('.swp'):
                    continue
                else:
                    pass
                # dummy clean flag
                _to_clean = True
                # prepare paths
                if INSTALL is True\
                or REMOVE is True:
                    _src_path = os.path.join(_p, _f)
                    _dst_path = os.path.join(_dst_dir, _f)
                else:
                    _src_path = os.path.join(_dst_dir, _f)
                    _dst_path = os.path.join(_p, _f)
                # ..
                _bck_path = os.path.join(_bck_dir, _f)
                try:
                    # check dst already exist
                    if os.path.exists(_dst_path):
                        # do backup
                        _copy_rights(_dst_path, _bck_path, 1000, 1000)
                    else:
                        pass
                    if REMOVE is True:
                        # remove previous
                        os.remove(_dst_path)
                        # DEBUG
                        print 'cleaned: %s' % _src_path
                    else:
                        # do copy
                        _copy_rights(_src_path, _dst_path, _uid, _gid)
                        # DEBUG
                        print 'updated: %s' % _src_path
                except Exception, e:
                    # DEBUG
                    print 'Ooops - %s: %s' % (_src_path, e)
            # remove dest dir if empty
            if REMOVE is True\
            and _to_clean is True\
            and os.path.exists(_dst_dir)\
            and len(os.listdir(_dst_dir)) == 0:
                os.removedirs(_dst_dir)
            else:
                pass


def remove_dir(dir_name, parent=None):
    # get activity path
    if parent is None:
        _dir = dir_name
        _next_parent = dir_name
    else:
        _dir = os.path.join(parent, dir_name)
        _next_parent = os.path.join(parent, dir_name)
    # remove files and dir recursively
    if os.path.exists(_dir):
        for _f in os.listdir(_dir):
            _p = os.path.join(_dir, _f)
            if os.path.isdir(_p):
                remove_dir(_f, parent=_next_parent)
            else:
                os.remove(_p)
        # and remove the dir
        if os.path.exists(_dir):
            # removed it
            os.removedirs(_dir)
        else:
            pass
    # nothing to do
    else:
        pass


if __name__ == '__main__':
    # little check
    if INSTALL is False\
    and SYNC is False\
    and REMOVE is False:
        exit(0)
    else:
        pass
    # sync paths
    _update_path('app')
    _update_path('skin')
    # change backup folder owner and permission
    os.chown(BCK_EXT_PATH, 1000, 1000)
    os.chmod(BCK_EXT_PATH, int(CHMOD))
    # change dir for tar stuff
    os.chdir(BACKUP_PATH)
    # prepare timestamp push flag and tar name
    _stamp = time.strftime('%Y%m%d_%H:%M:%S', time.localtime())
    if INSTALL is True:
        _type = 'push'
    elif SYNC is True:
        _type = 'pull'
    else:
        _type = 'clean'
    _tar_name = '%s_%s_%s.tar.gz' % (_stamp, _type, EXT_NAME)
    # tar the backup
    tar = tarfile.open(_tar_name, 'w:gz')
    tar.add(EXT_NAME)
    tar.close()
    # remove tmp dir
    remove_dir(BCK_EXT_PATH)
