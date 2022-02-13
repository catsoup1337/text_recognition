import pytesseract
import easyocr
from pixellib.instance import instance_segmentation
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

result = []


def object_detection_on_an_image(file_path):
    segment_image = instance_segmentation()
    segment_image.load_model(
        "put your path to mask_rcnn_coco.h5")
    target_class = segment_image.select_target_classes(person=True)
    result = segment_image.segmentImage(
        image_path=f'file_path}',
        # show_bboxes=True,
        segment_target_classes=target_class,
        extract_segmented_objects=True,
        save_extracted_objects=True,
        # output_image_name="output.jpg"
    )
    objects_count = len(result[0]["scores"])
    recognice(objects_count)


def recognice(objects_count):
    result.clear()
    for n in range(objects_count):
        rec_name = f'segmented_object_{n+1}.jpg'
        reader = easyocr.Reader(["ru", "en"])
        text = reader.readtext(
            rec_name, detail=0, allowlist='0123456789', paragraph=False)
        for i in range(len(text)):
            if len(text[i]) < 5:
                result.append(text[i])


def main(image):
    object_detection_on_an_image(file_path=image)
    return result


if __name__ == "__main__":
    main()
