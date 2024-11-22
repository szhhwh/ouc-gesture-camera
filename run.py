import cv2
import os

# 请根据需要更改以下三个参数
gesture_name = 'hello' # 手势名称
gesture_mark = 'P' # 手势字母标记（用于区分不同人的数据）
label = '0' # 手势数字标记（与customize_service.py中的数字标记保持一致）

counter = 0 # 计数器

def set_filename(parentdir ,extension):
    global counter

    def new_filename(parentdir, extension):
        filename = gesture_name + '_' + gesture_mark + str(counter)
        if extension != '':
            return parentdir + filename + '.' + extension
        else:
            return parentdir + filename
    
    filename = new_filename(parentdir, extension)
    while os.path.exists(filename):
        counter += 1
        filename = new_filename(parentdir, extension)

    return filename


def save_img_labeled(frame):
    global counter, label
    if not os.path.exists('./output'):
        os.mkdir('./output')
    
    cv2.imwrite(set_filename('./output/', 'jpg'), frame)
    with open(set_filename('./output/', 'txt'), 'a') as f:
        f.write(set_filename('', 'jpg') + ',' + label)

    counter += 1
    print("image saved %s" % set_filename('', 'jpg'))

def main():
    print("Hello from gesture-camera!")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法捕捉图像")
            break

        width = int(cap.get(3))
        height = int(cap.get(4))

        # 计算矩形的起点和终点
        x_start = max(0, int((width - 230) / 2))
        y_start = max(0, int((height - 230) / 2))
        x_end = min(x_start + 230, width)
        y_end = min(y_start + 230, height)

        # 在frame上绘制矩形
        cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 1)

        # 翻转帧
        frame = cv2.flip(frame, 1)

        # 显示整个frame，包含绘制的矩形
        cv2.imshow('Camera', frame)

        x_start_t = int((width - 224) / 2)
        y_start_t = int((height - 224) / 2)
        x_end_t = x_start + 224
        y_end_t = y_start + 224
        target = frame[y_start_t:y_end_t, x_start_t:x_end_t]

        key = cv2.waitKey(1)
        if key == ord('q'):  # 按下'q'键退出
            break
        elif key == ord('c'):  # 按下'c'键捕捉图像
            save_img_labeled(target)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
