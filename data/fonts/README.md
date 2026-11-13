# Mongolian Classical Fonts / Монгол Бичгийн Фонтууд

Энэхүү хавтсанд Монгол бичгийн албан ёсны TrueType/OpenType фонтуудыг багтаав.

## 1. Almas Inc. & Delehi Information Technology Co. Ltd. (2011–2015)
Эх сурвалж: [mongolfont.com](http://www.mongolfont.com/en/)

| Файлын нэр | Төрөл | Технологи | Тохирох систем | Тайлбар |
| :--- | :--- | :--- | :--- | :--- |
| `mnglartaat.ttf` | Art / Чимэглэлийн | AAT (Apple Advanced Typography) | macOS, iOS | Apple CoreText-д зориулсан AAT хэлбэр |
| `mnglartotf.ttf` | Art / Чимэглэлийн | OpenType (GSUB/GPOS/GDEF) | Windows, Linux, Web | OpenType стандарт хэлбэр |
| `mngltitleaat.ttf` | Title / Гарчгийн | AAT (Apple Advanced Typography) | macOS, iOS | Гарчиг, томоор бичихэд зориулсан |
| `mngltitleotf.ttf` | Title / Гарчгийн | OpenType (GSUB/GPOS/GDEF) | Windows, Linux, Web | Гарчиг, томоор бичихэд зориулсан |
| `mnglwhiteaat.ttf` | White / Цагаан | AAT (Apple Advanced Typography) | macOS, iOS | Стандарт бичвэрийн өргөн хэрэглээ |
| `mnglwhiteotf.ttf` | White / Цагаан | OpenType (GSUB/GPOS/GDEF) | Windows, Linux, Web | Стандарт бичвэрийн өргөн хэрэглээ |
| `mnglwritingaat.ttf` | Writing / Бичмэл | AAT (Apple Advanced Typography) | macOS, iOS | Бичмэл хэлбэрийн фонт |
| `mnglwritingotf.ttf` | Writing / Бичмэл | OpenType (GSUB/GPOS/GDEF) | Windows, Linux, Web | Бичмэл хэлбэрийн фонт |

## Шалгалт, Баталгаажуулалт (Verification)
- Бүх фонтуудыг `fontTools` болон FreeType / Pillow ашиглан шалгаж, хүснэгтийн бүтэц (cmap, glyf, OS/2, morx/GSUB), Unicode Mongolian Block (`U+1800`–`U+18AF`) дэмжлэг, дүрслэл (rendering) 100% алдаагүй болохыг туршиж баталгаажуулсан.

