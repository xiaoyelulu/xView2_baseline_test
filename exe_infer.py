# 环境：macosx、stackless python & twisted
import os
from os import path, walk, makedirs
json_path='/mnt/disk3/zwy/XBD/test/images/'
jsons = [j for j in next(walk(json_path))[2] if '_pre' in j]
for json in jsons:
    json1=json.replace('pre','post')
    #cmd = './utils/inference.sh -x /mnt/disk3/zwy/zwy/sematicseg/xView2_baseline-master/ -i /mnt/disk3/zwy/XBD/test/images/socal-fire_00001378_pre_disaster.tif -p /mnt/disk3/zwy/XBD/test/images/socal-fire_00001378_post_disaster.tif -l /mnt/disk3/zwy/zwy/sematicseg/xView2_baseline-master/spacenet/models/logs/model_iter_44800 -c /mnt/disk3/zwy/zwy/sematicseg/xView2_baseline-master/model/trail/-saved-model-100-0.72.hdf5 -o /mnt/disk3/zwy/zwy/sematicseg/xView2_baseline-master/infer_out/ -y'  # 全路径或者./相对路径
    cmd = './utils/inference.sh -x /mnt/disk3/zwy/zwy/sematicseg/xView2_baseline-master/ -i /mnt/disk3/zwy/XBD/test/images/'+json+ ' -p /mnt/disk3/zwy/XBD/test/images/'+json1+' -l /mnt/disk3/zwy/zwy/sematicseg/xView2_baseline-master/spacenet/models/logs/model_iter_44800 -c /mnt/disk3/zwy/zwy/sematicseg/xView2_baseline-master/model/trail/-saved-model-100-0.72.hdf5 -o /mnt/disk3/zwy/zwy/sematicseg/xView2_baseline-master/infer_out/ -y'  # 全路径或者./相对路径
    os.system(cmd)

