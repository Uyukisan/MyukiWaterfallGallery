# MyukiWaterfallGallery

>  A waterfall flow gallery plugin created with love.

## Usage

```html
<link rel="stylesheet" href="./css/MyukiWaterfallGallery.css">
<script src="./js/MyukiWaterfallGallery.js"></script>
```

```html
<script>
const MWG = $MWG({
  selector: ".container",
  /*
  selector: Container of Waterfall Flow Gallery.
  default: body
  */
  margin: "1rem",
  /*
  margin：margin of gallery.
  default: "1rem"
  */
  viewWidth: "80%",
  /*
  viewWidth：Maximum width of image preview.
  default: "80%"
  */
  col_spacing: "10px",
  /*
  col_spacing: Spacing between columns.
  default: "10px"
  */
  row_spacing: "10px",
  /*
  row_spacing: Spacing between rows.
  default: "10px"
  */
  lazyLoadSize: 20,
  /*
  lazyLoadSize: Size of lazy loading of images.
  default: 20
  */
});
MWG.loadImgList([{
		"title": "pixiv_68566145.png",
		"url": "https://img.hachiman.eu.org/pixiv_68566145.png",
		"size": "1.31MB",
		"width": 1968,
		"height": 1477,
		"color": [
			166,
			127,
			125
		]
	},
	{
		"title": "pixiv_80675375.jpg",
		"url": "https://img.hachiman.eu.org/pixiv_80675375.jpg",
		"size": "1.19MB",
		"width": 1200,
		"height": 1600,
		"color": [
			251,
			127,
			104
		]
	},
	{
		"title": "pixiv_50362556.png",
		"url": "https://img.hachiman.eu.org/pixiv_50362556.png",
		"size": "452.75KB",
		"width": 585,
		"height": 921,
		"color": [
			17,
			37,
			54
		]
	}
]);
/*
You can use waterfall_data_gen.py to generate the required image data list.
*/
</script>
```

## Preview

[MyukiWaterfallGallery](https://gallery.stackblog.cf)