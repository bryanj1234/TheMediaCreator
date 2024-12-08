# Notes

See:
  * https://platform.openai.com/docs/guides/text-generation
  * https://cookbook.openai.com/
    * https://cookbook.openai.com/examples/gpt_with_vision_for_video_understanding
    * etc...

## Goals

### First steps

* COMPLETED: ~~Sketch of images from text~~
  * `brylibimages.get_image_from_prompt(prompt)`
* IN-PROGRESS: Sketch of getting text from images. 
  * `brylibimages.get_text_from_image()`

### Movies from text

* Generate images from text
  * Figure out the best way to get text to feed to `brylibimages.get_image_from_prompt`
* Use images + text to make stories
* Use stories + images to make movies

### Movies from images

* Take a few images
* Get texts from the images
* Take the texts and combine into story
* Make movie

## Completed

* Initial sketch of `brylibimages.get_image_from_prompt(prompt)`