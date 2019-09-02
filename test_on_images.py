
from src import detect_faces, show_bboxes
from PIL import Image

# img = Image.open('images/office1.jpg')
# bounding_boxes, landmarks = detect_faces(img)
# im = show_bboxes(img, bounding_boxes, landmarks)
# img.show()
# im.show()

# img = Image.open('images/office2.jpg')
# bounding_boxes, landmarks = detect_faces(img)
# im = show_bboxes(img, bounding_boxes, landmarks)
# img.show()
# im.show()


# img = Image.open('images/office3.jpg')
# bounding_boxes, landmarks = detect_faces(img)
# im = show_bboxes(img, bounding_boxes, landmarks)
# img.show()
# im.show()


# img = Image.open('images/office4.jpg')
# bounding_boxes, landmarks = detect_faces(img, thresholds=[0.6, 0.7, 0.85])
# im = show_bboxes(img, bounding_boxes, landmarks)
# img.show()
# im.show()


img = Image.open('images/office5.jpg')
bounding_boxes, landmarks = detect_faces(img, min_face_size=10)
im = show_bboxes(img, bounding_boxes, landmarks)
im.show()


