import glob
from PIL import Image

class GifConverter:
    def __init__(self, path_in=None, path_out=None, resize=(320, 240)):
        """
        path_in  : 원본 여러 이미지 경로(Ex : images/*.png)
        path_out : 결과 이미지 경로(Ex : output/filename.gif)
        resize   : 리사이징 크기((320,240))
        아래의 or부분은 기본값을 설정하는 부분이다. (입력하지 않았을때를 대비)
        """
        self.path_in = path_in or './*.png'
        self.path_out = path_out or './output.gif'
        self.resize = resize
    
    def convert_gif(self):
        """
        GIF 이미지 변환 기능 수행
        """
        print(self.path_in, self.path_out, self.resize)

        img, *images = \
        [Image.open(f).resize(self.resize, Image.Resampling.LANCZOS) for f in sorted(glob.glob(self.path_in))]
        try:
            new_images = []

            for image in images:
                new_image = Image.new("RGBA", img.size)
                new_image.paste(image, (0, 0), image)
                new_images.append(new_image.convert("RGBA"))

            img = img.convert("RGBA")

            img.save(
                fp=self.path_out, 
                format='GIF', 
                append_images=new_images,
                save_all=True, 
                duration=500, 
                loop=0,
                transparency=1,
                disposal=2
            )
        except IOError:
            print("Cannot convert!", img)
         
if __name__ == "__main__":
	# 클래스 테스트
	c = GifConverter("./project/images/*.png", './project/image_out/result2.gif', (320,240))
	# 변환
	c.convert_gif()