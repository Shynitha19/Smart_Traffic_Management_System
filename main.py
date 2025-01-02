from utils.video_utils import read_video, save_video, detect_vehicles
from model.objectTracker.tracker import Tracker

def main():

    frames = read_video("C:\\Users\\Balam\\OneDrive\\Documents\\project\\18 Nov Code\\traffic_video.mp4")

    #object tracking
    obj_tracker = Tracker()
    result = obj_tracker.detect_objects(frames)

    output_frames = obj_tracker.draw_annotations(frames, result)


    save_video(output_frames, "C:\\Users\\Balam\\OneDrive\\Desktop\\Infosys_springboard\\Smart_Traffic_Management_System\\result\\output.avi")

if __name__ == '__main__':
    main()