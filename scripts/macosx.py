#coding:utf-8
import shutil
import os, stat
import subprocess
Import("env","projenv")

if os.path.isfile(projenv.subst("$BUILD_DIR/$PROGNAME$PROGSUFFIX")):
    os.remove(projenv.subst("$BUILD_DIR/$PROGNAME$PROGSUFFIX"))
def copyFiles(src_dir, dst_dir):
    for foldername, subfolders, filenames in os.walk(src_dir):
        for filename in filenames:
            if filename.endswith(".dll"):
                src_file = os.path.join(foldername, filename)
                dst_file = os.path.join(dst_dir, filename)

                if os.path.isfile(dst_file):
                    continue
                shutil.copyfile(src_file, dst_file)
def mkdir(path):
	folder = os.path.exists(path)
	if not folder:
		os.makedirs(path)
def post_program_action(source, target, env):
    mkdir("./build")
    if os.path.isfile(projenv.subst("$BUILD_DIR/$PROGNAME$PROGSUFFIX")):
        shutil.copyfile(projenv.subst("$BUILD_DIR/$PROGNAME$PROGSUFFIX"), "./build/fltk")
        os.chmod("./build/fltk", stat.S_IXUSR)
        p = subprocess.Popen("./build/fltk")
        p.wait()
        
env.AddPostAction("$PROGPATH", post_program_action)