# import ast
#
# import cv2
# import numpy as np
# import pandas as pd
#
# results = pd.read_csv('test1_testing.csv')
#
# # load video
# video_path = 'data/main.mp4'
# cap = cv2.VideoCapture(video_path)
#
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# out = cv2.VideoWriter('./out1_testing_without_interpolation.mp4', fourcc, fps, (width, height))
#
#
# license_plate = {}
# for car_id in np.unique(results['car_id']):
#     max_ = np.amax(results[results['car_id'] == car_id]['license_number_score'])
#
#     license_plate[car_id] = {'license_crop': None,
#                              'license_plate_number': results[(results['car_id'] == car_id) &
#                                                              (results['license_number_score'] == max_)]['license_number'].iloc[0]}
#
#     # When you use cv2.CAP_PROP_POS_FRAMES, you are telling OpenCV to jump to a specific frame in the video stream.
#     cap.set(cv2.CAP_PROP_POS_FRAMES, results[(results['car_id'] == car_id) &
#                                              (results['license_number_score'] == max_)]['frame_nmr'].iloc[0])
#     ret, frame = cap.read()
#
#     x1, y1, x2, y2 = ast.literal_eval(results[(results['car_id'] == car_id) &
#                                               (results['license_number_score'] == max_)]['license_plate_bbox'].iloc[0].replace('[ ', '[').replace('   ', ' ').replace('  ', ' ').replace(' ', ','))
#
#     license_crop = frame[int(y1):int(y2), int(x1):int(x2), :]
#
#     license_crop = cv2.resize(license_crop, (int((x2 - x1) * 400 / (y2 - y1)), 400))
#
#     license_plate[car_id]['license_crop'] = license_crop
#
#
# frame_nmr = -1
#
# cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#
# # read frames
# ret = True
# while ret:
#     ret, frame = cap.read()
#     frame_nmr += 1
#     if ret:
#         df_ = results[results['frame_nmr'] == frame_nmr]
#         for row_indx in range(len(df_)):
#             # draw car
#             car_x1, car_y1, car_x2, car_y2 = ast.literal_eval(df_.iloc[row_indx]['car_bbox'].replace('[ ', '[').replace('   ', ' ').replace('  ', ' ').replace(' ', ','))
#
#             cv2.rectangle(frame, (int(car_x1), int(car_y1)), (int(car_x2), int(car_y2)), (0, 255, 0), 2)
#
#             # draw license plate
#             x1, y1, x2, y2 = ast.literal_eval(df_.iloc[row_indx]['license_plate_bbox'].replace('[ ', '[').replace('   ', ' ').replace('  ', ' ').replace(' ', ','))
#             cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 1)
#
#
#
#             try:
#                 cv2.putText(frame,
#                             license_plate[df_.iloc[row_indx]['car_id']]['license_plate_number'],
#                             (int(car_x1), int(car_y1)),
#                             cv2.FONT_HERSHEY_SIMPLEX,
#                             1,
#                             (0, 0, 0),
#                             2)
#             except:
#                 pass
#
#         out.write(frame)
#         frame = cv2.resize(frame, (1280, 720))
#
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#         # cv2.waitKey(0)
#
# out.release()
# cap.release()
#
#
#


import ast
import cv2
import numpy as np
import pandas as pd

results = pd.read_csv("C:\\Users\\Balam\\OneDrive\\Desktop\\Infosys_springboard\\Smart_Traffic_Management_System\\output\\verticle_testing.csv")

# load video
video_path = "C:\\Users\\Balam\\OneDrive\\Documents\\ANPR_and_ATCC_for_Smart_Traffic_Management\\videos\\2103099-uhd_2560_1440_30fps.mp4"
cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter("C:\\Users\\Balam\\OneDrive\\Desktop\\Infosys_springboard\\Smart_Traffic_Management_System\\result\\output_1.avi", fourcc, fps, (width, height))

license_plate = {}

for car_id in np.unique(results['car_id']):
    max_ = np.amax(results[results['car_id'] == car_id]['license_number_score'])

    license_plate[car_id] = {'car_class': results[(results['car_id'] == car_id) &
                                                             (results['license_number_score'] == max_)]['car_class'].iloc[0],
                             'license_plate_number': results[(results['car_id'] == car_id) &
                                                             (results['license_number_score'] == max_)]['license_number'].iloc[0]}

frame_nmr = -1

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# read frames
ret = True
while ret:
    ret, frame = cap.read()
    frame_nmr += 1
    if ret:
        df_ = results[results['frame_nmr'] == frame_nmr]
        for row_indx in range(len(df_)):
            # draw car
            car_x1, car_y1, car_x2, car_y2 = ast.literal_eval(df_.iloc[row_indx]['car_bbox'].replace('[ ', '[').replace('   ', ' ').replace('  ', ' ').replace(' ', ','))

            # Updated color dictionary
            color_dict = {
                "car": (255, 165, 0),  # Orange
                "bus": (75, 0, 130),   # Indigo
                "truck": (0, 255, 255), # Cyan
                "motorcycle": (128, 0, 128), # Purple
                "0": (255, 20, 147)   # DeepPink
            }
            object_class_name = license_plate[df_.iloc[row_indx]['car_id']]['car_class']
            object_color = color_dict.get(object_class_name, (255, 255, 255))  # Default to white if class not found

            cv2.rectangle(frame, (int(car_x1), int(car_y1)), (int(car_x2), int(car_y2)), object_color, 2)

            # draw license plate
            x1, y1, x2, y2 = ast.literal_eval(df_.iloc[row_indx]['license_plate_bbox'].replace('[ ', '[').replace('   ', ' ').replace('  ', ' ').replace(' ', ','))
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), 1)  # License plate border color set to white

            try:
                cv2.putText(frame,
                            f"{object_class_name}: {license_plate[df_.iloc[row_indx]['car_id']]['license_plate_number']}",
                            (int(car_x1), int(car_y1)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            object_color,
                            2)
            except:
                pass

        out.write(frame)

out.release()
cap.release()