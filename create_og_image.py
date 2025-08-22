#!/usr/bin/env python3
"""
Open Graph Image Generator
Creates a 1200x630 pixel image suitable for social media sharing
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_og_image(input_image_path, output_path="og-image.png", title="Git & GitHub for Beginners"):
    """
    Create an Open Graph image from an input image
    
    Args:
        input_image_path (str): Path to the input image
        output_path (str): Path for the output OG image
        title (str): Title text to overlay on the image
    """
    
    # Open Graph image dimensions (Facebook, Twitter, LinkedIn standard)
    og_width = 1200
    og_height = 630
    
    try:
        # Open the input image
        with Image.open(input_image_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize the image to fit within OG dimensions while maintaining aspect ratio
            img.thumbnail((og_width, og_height), Image.Resampling.LANCZOS)
            
            # Create a new image with OG dimensions and a dark background
            og_image = Image.new('RGB', (og_width, og_height), (18, 18, 18))
            
            # Calculate position to center the image
            x_offset = (og_width - img.width) // 2
            y_offset = (og_height - img.height) // 2
            
            # Paste the resized image onto the background
            og_image.paste(img, (x_offset, y_offset))
            
            # Add a semi-transparent overlay for better text readability
            overlay = Image.new('RGBA', (og_width, og_height), (0, 0, 0, 100))
            og_image = Image.alpha_composite(og_image.convert('RGBA'), overlay).convert('RGB')
            
            # Add title text
            draw = ImageDraw.Draw(og_image)
            
            # Try to use a system font, fallback to default if not available
            try:
                # Try to find a suitable font
                font_size = 48
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
            except:
                try:
                    font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()
            
            # Calculate text position (centered)
            bbox = draw.textbbox((0, 0), title, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_x = (og_width - text_width) // 2
            text_y = og_height - text_height - 50
            
            # Draw text with outline for better visibility
            outline_color = (0, 0, 0)
            text_color = (255, 255, 255)
            
            # Draw outline
            for dx in [-2, -1, 0, 1, 2]:
                for dy in [-2, -1, 0, 1, 2]:
                    draw.text((text_x + dx, text_y + dy), title, font=font, fill=outline_color)
            
            # Draw main text
            draw.text((text_x, text_y), title, font=font, fill=text_color)
            
            # Save the OG image
            og_image.save(output_path, 'PNG', quality=95)
            print(f"✅ Open Graph image created successfully: {output_path}")
            print(f"   Dimensions: {og_width}x{og_height} pixels")
            print(f"   Format: PNG")
            
    except FileNotFoundError:
        print(f"❌ Error: Input image not found at {input_image_path}")
    except Exception as e:
        print(f"❌ Error creating OG image: {str(e)}")

def main():
    """Main function to create OG image from the attached JPEG"""
    
    # Input image path (the attached JPEG)
    input_image = "_6a954c68-9bda-49d3-be7d-ceb91ddd88eb.jpeg"
    
    # Check if input image exists
    if not os.path.exists(input_image):
        print(f"❌ Input image not found: {input_image}")
        return
    
    # Create OG image
    create_og_image(
        input_image_path=input_image,
        output_path="og-image.png",
        title="Git & GitHub for Beginners"
    )

if __name__ == "__main__":
    main()
