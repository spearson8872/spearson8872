from PIL import Image
from PIL.ExifTags import TAGS


def read_jpg_comments(image_path):
    try:
        image = Image.open(image_path)
        exifdata = image.getexif()

        if exifdata:
            print(f"Metadata for {image_path}:")
            for tag_id in exifdata:
                tag_name = TAGS.get(tag_id, tag_id)
                value = exifdata.get(tag_id)

                # Check for comment-related tags, or print all for inspection

                if "XPComment" in tag_name:
                    this_value = value.replace(b"\x00", b"")
                    print(f"{tag_name}: {this_value}")

                # if "Comment" in tag_name or "UserComment" in tag_name:
                #   print(f"{tag_name}: {value}")
                # You can also print all tags to see what's available
                #print(f"{tag_name}: {value}")
        else:
            print(f"No EXIF data found in {image_path}.")

    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
read_jpg_comments(r"C:/temp/photos/test (1).jpg")