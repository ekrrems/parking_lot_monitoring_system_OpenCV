import cv2
import pickle


# print(img.shape)
try:
    with open('car_park_pos', 'rb') as f:
        pos_list = pickle.load(f)

except:
    pos_list = []

width, height = 27, 15


def click_event(event, x, y ,flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        pos_list.append((x, y))

    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(pos_list):
            x1, y1 = pos
            if x1 < x < x1+ width and y1 < y < y1 + height:
                pos_list.pop(i)

    with open('car_park_pos', 'wb') as f:
        pickle.dump(pos_list, f)


while 1:
    img = cv2.imread("busy_lot.png")

    for pos in pos_list:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 1)

    cv2.imshow('img', img)
    cv2.setMouseCallback('img', click_event)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()