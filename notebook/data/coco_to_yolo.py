import json
import os

def coco_to_yolo(coco_json_path, output_dir="labels_yolo", class_name="probe"):
    # Load COCO annotations
    with open(coco_json_path, "r") as f:
        data = json.load(f)

    # 1) Map the class name to a class ID
    class_mapping = {class_name: 0}

    # 2) Create a lookup table for images
    image_lookup = {}
    for img in data["images"]:
        img_id = img["id"]
        image_lookup[img_id] = (
            img["width"],
            img["height"],
            img["file_name"]
        )

    # 3) Prepare an output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 4) Gather YOLO lines for each image
    yolo_dict = {}  # Key: file_name, Value: list of YOLO lines
    for ann in data["annotations"]:
        image_id = ann["image_id"]
        bbox = ann["bbox"]  # [x, y, w, h]
        
        # Retrieve image details
        img_width, img_height, file_name = image_lookup[image_id]

        # Extract x, y, w, h
        x, y, w, h = bbox
        x_center = x + w/2
        y_center = y + h/2

        # Normalize
        x_center_norm = x_center / img_width
        y_center_norm = y_center / img_height
        w_norm = w / img_width
        h_norm = h / img_height

        # Assign class_id based on the class name (always "probe" in this case)
        class_id = class_mapping[class_name]

        # Format the YOLO line
        yolo_line = f"{class_id} {x_center_norm:.6f} {y_center_norm:.6f} {w_norm:.6f} {h_norm:.6f}"

        # Append to dictionary
        if file_name not in yolo_dict:
            yolo_dict[file_name] = []
        yolo_dict[file_name].append(yolo_line)

    # 5) Write one .txt label file per image
    for file_name, lines in yolo_dict.items():
        base_name, _ = os.path.splitext(file_name)
        txt_file_path = os.path.join(output_dir, f"{base_name}.txt")
        with open(txt_file_path, "w") as txt_file:
            txt_file.write("\n".join(lines))

    print(f"✅ Conversion complete! YOLO labels saved in: {output_dir}")

# USAGE EXAMPLE
coco_to_yolo("notebook/probe_labels.json", output_dir="notebook/labels_yolo_Probe", class_name="probe")
