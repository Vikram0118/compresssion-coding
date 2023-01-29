# import cv2

# src_dir = "./video.mp4"
# dst_dir = "./output.avi"

# video_cap = cv2.VideoCapture(src_dir)
# fps = video_cap.get(cv2.CAP_PROP_FPS)

# fps = video_cap.get(cv2.CAP_PROP_FPS)
# size = (int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH)),   
#         int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  
# #video_writer = cv2.VideoWriter_fourcc(dst_dir, cv2.FOURCC('M', 'J', 'P', 'G'), fps, size) 
# video_writer = cv2.VideoWriter(dst_dir, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size) 

# success, frame = video_cap.read()
# while success:
#     video_writer.write(frame)
#     success, frame = video_cap.read()

import imageio

src_dir = "./video.mp4"
dst_dir = "./output2.avi"

reader = imageio.get_reader(src_dir)
fps = reader.get_meta_data()['fps']
writer = imageio.get_writer(dst_dir, fps=fps)

for im in reader:
    writer.append_data(im[:, :, :])
writer.close()