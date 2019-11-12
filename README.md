This API will convert your image into a super resolution image.

Providing the low resolution image url to the API will returns the conversion of your image into a super resolution image.

- - -

Read these papers to learn more about segmentation technics:

[SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation](https://arxiv.org/abs/1511.00561)
```
@article{DBLP:journals/corr/BadrinarayananK15,
  author    = {Vijay Badrinarayanan and
               Alex Kendall and
               Roberto Cipolla},
  title     = {SegNet: {A} Deep Convolutional Encoder-Decoder Architecture for Image
               Segmentation},
  journal   = {CoRR},
  volume    = {abs/1511.00561},
  year      = {2015},
  url       = {http://arxiv.org/abs/1511.00561},
  archivePrefix = {arXiv},
  eprint    = {1511.00561},
  timestamp = {Mon, 13 Aug 2018 16:46:06 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/BadrinarayananK15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
[Fully Convolutional Networks for Semantic Segmentation](https://arxiv.org/abs/1411.4038)
```
@article{DBLP:journals/corr/LongSD14,
  author    = {Jonathan Long and
               Evan Shelhamer and
               Trevor Darrell},
  title     = {Fully Convolutional Networks for Semantic Segmentation},
  journal   = {CoRR},
  volume    = {abs/1411.4038},
  year      = {2014},
  url       = {http://arxiv.org/abs/1411.4038},
  archivePrefix = {arXiv},
  eprint    = {1411.4038},
  timestamp = {Mon, 13 Aug 2018 16:48:17 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/LongSD14},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

[U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597)
```
@article{DBLP:journals/corr/RonnebergerFB15,
  author    = {Olaf Ronneberger and
               Philipp Fischer and
               Thomas Brox},
  title     = {U-Net: Convolutional Networks for Biomedical Image Segmentation},
  journal   = {CoRR},
  volume    = {abs/1505.04597},
  year      = {2015},
  url       = {http://arxiv.org/abs/1505.04597},
  archivePrefix = {arXiv},
  eprint    = {1505.04597},
  timestamp = {Mon, 13 Aug 2018 16:46:52 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/RonnebergerFB15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
[Pyramid Scene Parsing Network](https://arxiv.org/abs/1612.01105)
```
@article{DBLP:journals/corr/ZhaoSQWJ16,
  author    = {Hengshuang Zhao and
               Jianping Shi and
               Xiaojuan Qi and
               Xiaogang Wang and
               Jiaya Jia},
  title     = {Pyramid Scene Parsing Network},
  journal   = {CoRR},
  volume    = {abs/1612.01105},
  year      = {2016},
  url       = {http://arxiv.org/abs/1612.01105},
  archivePrefix = {arXiv},
  eprint    = {1612.01105},
  timestamp = {Mon, 13 Aug 2018 16:47:16 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/ZhaoSQWJ16},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
- - -

EXAMPLE  
![example](https://i.ibb.co/PNMfns7/example.png)  

- - -

INPUT

``` json
{
  "url": "https://i.ibb.co/6X88r2n/input.png",
  "model": "scene_parsing"
}
```

- - -

EXECUTION

``` bash
curl -X POST "https://api-market-place.ai.ovh.net/image-segmentation/process" -H "accept: application/json" -H "X-OVH-Api-Key: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" -H "Content-Type: application/json" -d '{"url":"https://i.ibb.co/6X88r2n/input.png", "model": "scene_parsing"}'
```

- - -

OUTPUT

![output](https://i.ibb.co/58Xh7Tv/output.png)

please refer to swagger documentation for further technical details: [swagger documentation](https://market-place.ai.ovh.net/#!/apis/1434153e-9eef-4080-b415-3e9eef408004/pages/b86f91d0-8b8b-4e47-af91-d08b8b3e47e8)
