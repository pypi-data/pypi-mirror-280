from PIL import Image
import requests

def help_():
    print("""1. Понятие машинного обучения. Отличие машинного обучения от других
областей программирования.
2. Классификация задач машинного обучения. Примеры задач из
различных классов.
3. Основные понятия машинного обучения: набора данных, объекты,
признаки, атрибуты, модели, параметры.
4. Структура и представление данных для машинного обучения.
5. Инструментальные средства машинного обучения.
6. Задача регрессии: постановка, математическая формализация.
7. Метод градиентного спуска для парной линейной регрессии.
8. Понятие функции ошибки: требования, использование, примеры.
9. Множественная и нелинейная регрессии.
10.Нормализация признаков в задачах регрессии.
11.Задача классификации: постановка, математическая формализация.
12.Метод градиентного спуска для задач классификации.
13.Логистическая регрессия в задачах классификации.
14.Множественная и многоклассовая классификация. Алгоритм “один
против всех”.
15.Метод опорных векторов в задачах классификации.
16.Понятие ядра и виды ядер в методе опорных векторов.
17.Метод решающих деревьев в задачах классификации.
18.Метод k ближайших соседей в задачах классификации.
19.Однослойный перцептрон в задачах классификации.
20.Метрики эффективности и функции ошибки: назначение, примеры,
различия.
21.Понятие набора данных (датасета) в машинном обучении. Требования,
представление. Признаки и объекты.
22.Шкалы измерения признаков. Виды шкал, их характеристика.
23.Понятие чистых данных. Определение, очистка данных.
24.Основные этапы проекта по машинному обучению.
25.Предварительный анализ данных: задачи, методы, цели.
26.Проблема отсутствующих данных: причины, исследование, пути
решения.
27.Проблема несбалансированных классов: исследование, пути решения.
28.Понятие параметров и гиперпараметров модели. Обучение параметров
и гиперпараметров. Поиск по сетке.
29.Понятие недо- и переобучения. Определение, пути решения.
30.Диагностика модели машинного обучения. Методы, цели.
31.Проблема выбора модели машинного обучения. Сравнение моделей.
32.Измерение эффективности работы моделей машинного обучения.
Метрики эффективности.
33.Метрики эффективности моделей классификации. Виды,
характеристика, выбор.
34.Метрики эффективности моделей регрессии. Виды, характеристика,
выбор.
35.Перекрестная проверка (кросс-валидация). Назначение, схема работы.
36.Конвейеры в библиотеке sklearn. Назначение, использование.
37.Использование методов визуализации данных для предварительного
анализа.
38.Исследование коррелированности признаков: методы, цели, выводы.
39.Решкалирование данных. Виды, назначение, применение.
Нормализация и стандартизация данных.
40.Преобразование категориальных признаков в числовые.
41.Методы визуализации данных для машинного обучения.
42.Задача выбора модели. Оценка эффективности, валидационный набор.
43.Кривые обучения для диагностики моделей машинного обучения.
44.Регуляризация моделей машинного обучения. Назначение, виды,
формализация.
45.Проблема сбора и интеграции данных для машинного обучения.
46.Понятие чистых данных и требования к данным.
47.Основные задачи описательного анализа данных.
48.Полиномиальные модели машинного обучения.
49.Основные виды преобразования данных для подготовки к машинному
обучению.
50.Задача выбора признаков в машинном обучении.""")

def v_1():
    im = Image.open(requests.get('https://sun9-36.userapi.com/impg/LUV9mZhM8VpMK7-EqXcTfvmE7tTafiXUOI1DQg/Fpb9vzre1Kc.jpg?size=636x598&quality=96&sign=3b4fce618abf9d3b01ba51fde9d10895&type=album', stream=True).raw)
    return im

def v_2():
    im = Image.open(requests.get('https://sun9-33.userapi.com/impg/nakAAe9zJ8f3jaJ2koVtC5hGZe7pRvzJkoLfGw/FVV6dP60JcI.jpg?size=820x763&quality=96&sign=af79579dff452002eff7165d7afff702&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-35.userapi.com/impg/bklrsxf5u-wN-7uGmJ7nQbz8IT1um6HRJI-C2A/2-AHW419WPo.jpg?size=780x301&quality=96&sign=7f2b31741b4af7c5a6c8803ec4319ca1&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-19.userapi.com/impg/JMPg-NTOHRCytsuBucTXt-vahgdCg2rUeXdRzA/lCmWXC8pyWE.jpg?size=807x275&quality=96&sign=8456767984ff5b032a54456b4483eb8d&type=album', stream=True).raw)
    return im, im2, im3

def v_3():
    im = Image.open(requests.get('https://sun9-78.userapi.com/impg/BLRAk3encFIh2yosS5Wq3milLefTIQvdZBTaPQ/PQN4SzagZZo.jpg?size=727x662&quality=96&sign=bb04f01be235253f294ec6071a483a0c&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun1-88.userapi.com/impg/XL9AvWWVwnNZYwUx6e6ufXHHXILKkYsVMbs9lA/pOGwelzWEzM.jpg?size=715x263&quality=96&sign=5b75d19b1ed668181c6d39f4055ead7d&type=album', stream=True).raw)
    return im, im2

def v_4():
    im = Image.open(requests.get('https://sun9-78.userapi.com/impg/9yMeHnrnizMN83SHyrGh2dL5yVCKRw4PPopPug/KvX0oQxw-q8.jpg?size=719x644&quality=96&sign=41c72b9627d92b9aa0884f71b6815f9b&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-68.userapi.com/impg/zpRrD_Jxmw4l012CxIyz75VoI4JC-Nd3Ql1bwA/Ru1wouvap3s.jpg?size=724x720&quality=96&sign=545b73fa895f8a32d1f221bd823031a3&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-13.userapi.com/impg/SsKMOKzxt2k8bTK4yn9q-znaKAvgA1CDQq1V6w/hg4LMkBA5vg.jpg?size=667x423&quality=96&sign=f2b8c2fbd0f24baf671fff5fe3272245&type=album', stream=True).raw)
    return im, im2, im3

def v_5():
    im = Image.open(requests.get('https://sun9-54.userapi.com/impg/FmwEMZdo0z7_9wig6k0BpN_cmbUjsf8dkmWiwg/Y9mYNXyq4B8.jpg?size=716x483&quality=96&sign=83aa1f5db80c6bf428cd346e45989451&type=album', stream=True).raw)
    return im

def v_6():
    im = Image.open(requests.get('https://sun1-90.userapi.com/impg/EcNb8EUBkWIn-LpVARIbvXtdfr59HZMdtq5obQ/MT_cx7IVgZs.jpg?size=727x270&quality=96&sign=1c2e9f3371d682c33f9229f6638dde65&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-50.userapi.com/impg/v9dGGCj2_rcP-dZxLG5KsKDJ3jL-4D_ikV5mYw/_NuB1Ibpy6Y.jpg?size=719x495&quality=96&sign=47e215dd6a3f7ab0f3196c5700ae6b1f&type=album', stream=True).raw)
    return im, im2

def v_7():
    im = Image.open(requests.get('https://sun9-12.userapi.com/impg/Pb60DVxr1pgK4O_Pi9g_WFZ8rAbsvul3vVNXwA/jTzjPH0G4Dk.jpg?size=644x211&quality=96&sign=50747711073b28600a41eb46b13cdb39&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-58.userapi.com/impg/pG44_RnphkSnBtD-o2XRyu0iaZ8z_zG7dL8Pww/rQLySouRQw0.jpg?size=555x420&quality=96&sign=526c30c176e5bf2558d94ec98a4c7606&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-1.userapi.com/impg/5Vhusu_tie8el_-jokKSGnijkCwKO8o4mTEqAw/SCwQIrtt0kA.jpg?size=572x234&quality=96&sign=3468b7f0fd6d39f01c729298f4c0ba8b&type=album', stream=True).raw)
    im4 = Image.open(requests.get('https://sun9-18.userapi.com/impg/pneEIkrshQK2_ANs5rMG8RG_8bubvbqYU0XggQ/6-7jZcTzuFY.jpg?size=547x638&quality=96&sign=027696c4efb02c6a91c6ddc36a0762df&type=album', stream=True).raw)
    im5 = Image.open(requests.get('https://sun9-65.userapi.com/impg/aTqbxTKlxCjx7ghWRpnPpZu9i2VE9eUi6w0wYw/urHWpUueRq4.jpg?size=614x688&quality=96&sign=33102dae6019867d5d823dcf2c7fa75c&type=album', stream=True).raw)
    im6 = Image.open(requests.get('https://sun9-66.userapi.com/impg/abbbKShzpJf4eOTBVIKYaR5IJwmRfV7SJYbZyA/3d5KlpbgbjI.jpg?size=381x266&quality=96&sign=f5115e753d2894c8ce4b782db8e426c7&type=album', stream=True).raw)
    im7 = Image.open(requests.get('https://sun9-33.userapi.com/impg/AbagLh3Uz_6YsFAoRsTuGDH5UVtpB-hq5qv7Vw/e8ik31MVviE.jpg?size=620x530&quality=96&sign=af538a03e8908309dfef7e5c5539bca4&type=album', stream=True).raw)
    return im, im2, im3, im4, im5, im6, im7

def v_8():
    im = Image.open(requests.get('https://sun9-51.userapi.com/impg/XX8CaLlf-kvW5jMPkYxrZR2wNhicQFlpIt4SmA/3hD0xE37y6c.jpg?size=730x154&quality=96&sign=95b995d990eb4fa6c3e306c7eb931a25&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-38.userapi.com/impg/Qq3OiTbHx4Lk2D2MlGj8pZGh2cQ6acVeO707jw/uIYhIuSHydw.jpg?size=715x459&quality=96&sign=109173fdd2c663e1d9087489075faeed&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-47.userapi.com/impg/CumVp02wEUc0QpSGs1m1-yCYvPkwfCSt8p_Gsw/tecDlQjzM18.jpg?size=704x474&quality=96&sign=67151739654aac96e2835c0560372217&type=album', stream=True).raw)
    im4 = Image.open(requests.get('https://sun9-16.userapi.com/impg/gW6WGGnC7-xNvTXs7eMnzIsh0mrAKDamVfPpWA/NwRlofytRjM.jpg?size=714x659&quality=96&sign=b23dee9c66754f9d5bce58834cae9998&type=album', stream=True).raw)
    im5 = Image.open(requests.get('https://sun9-16.userapi.com/impg/gW6WGGnC7-xNvTXs7eMnzIsh0mrAKDamVfPpWA/NwRlofytRjM.jpg?size=714x659&quality=96&sign=b23dee9c66754f9d5bce58834cae9998&type=album', stream=True).raw)
    return im, im2, im3, im4, im5

def v_9():
    im = Image.open(requests.get('https://sun9-76.userapi.com/impg/JOvKo89vfaIYTxkwYzRDfBc7P4rF1XOw4w8HBg/AgOkaRKsGqM.jpg?size=717x621&quality=96&sign=91db360d86c19b36abe0e4ea60a73a45&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-30.userapi.com/impg/yPa8UqFNCQWmssOtIVgKl5775bDx0S01xU7PGw/yWlPdeL6NhU.jpg?size=744x700&quality=96&sign=80e15fe3c1de563edc1a9a034f92ab01&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-19.userapi.com/impg/Fjrfe3X3_URgGfQE_RHAVqC_4FGCuX70ylbIjQ/Hph8yAZIEJw.jpg?size=731x690&quality=96&sign=5527ef4833fe7fe3a1ddf2cd78b02ab7&type=album', stream=True).raw)
    im4 = Image.open(requests.get('https://sun9-79.userapi.com/impg/lxno1K1yGmqNg1x0NNBYQw0WW-xMDarYtKKNdA/0U-iDfUifco.jpg?size=714x199&quality=96&sign=32c53f7c6b7624a58488a9478d8ddcda&type=album', stream=True).raw)
    return im, im2, im3, im4

def v_10():
    im = Image.open(requests.get('https://sun9-1.userapi.com/impg/SGN2udvNVDVIDx2wiZqL4A_fUVjVTteyKT6c9g/3vYK9Snm-HQ.jpg?size=685x525&quality=96&sign=3f33d89d0e8950321517050fca585ffe&type=album', stream=True).raw)
    return im

def v_11():
    im = Image.open(requests.get('https://sun9-46.userapi.com/impg/J2B2dLZrfUN6P7vYzDzu2nmXn7_bYfDPBYmYnw/adIHzxQa4YI.jpg?size=719x406&quality=96&sign=a56e56572e109db55b60b6293b11410c&type=album', stream=True).raw)
    return im

def v_12():
    im = Image.open(requests.get('https://sun9-44.userapi.com/impg/fYKnFCNDjU-WvOvwE3vfsy5VREwa2A0X2NbPag/EWXu6eBrUmM.jpg?size=726x677&quality=96&sign=33eb5a29d7c4c0a984a26011a116a990&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-74.userapi.com/impg/OuGpxl-oKtr9x1wDfwa4-Wwp1zCfSyCLh0jjJQ/1Q8iH05yI-8.jpg?size=729x652&quality=96&sign=07bc4388f87acc348e67f56de5d068b3&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-77.userapi.com/impg/-YDqsE_p8ojgXwwJjascRR0TOubyrf7jE4T1Sw/aQxL6JviuSE.jpg?size=693x252&quality=96&sign=837e971f5b65451fe39dc26c2640045c&type=album', stream=True).raw)
    return im, im2, im3

def v_13():
    im = Image.open(requests.get('https://sun9-50.userapi.com/impg/n9wx_Hoc6DkkkllQXzq3mcTdPW4ZF834msTTbQ/6wzI31r3qsQ.jpg?size=732x584&quality=96&sign=8138537b17ad89367f9cd69eec4a2c0b&type=album', stream=True).raw)
    return im

def v_14():
    im = Image.open(requests.get('https://sun9-79.userapi.com/impg/aRFd2PC-nDGsWEpWUQwFhTMeowznaigulSgcJg/GEA8cF6vJPU.jpg?size=704x444&quality=96&sign=954bba655cc7eaec7d09028674d213d7&type=album', stream=True).raw)
    return im

def v_15():
    im = Image.open(requests.get('https://sun9-60.userapi.com/impg/vefDYWupeyBJ_nq3OyN22cr_9RIa6euYX6IXrQ/zPHBZ7HTRBk.jpg?size=677x672&quality=96&sign=e68c5d3c3e2254b0434c10fb3bf7fdb8&type=album', stream=True).raw)
    return im

def v_16():
    im = Image.open(requests.get('https://sun9-44.userapi.com/impg/gLe8wxh1AKbaje5-ilWLenu6AKTdASc8g3tWgQ/u2tOPkK0rcE.jpg?size=803x367&quality=96&sign=24f0a5134a510455f1abdda114bfd3b5&type=album', stream=True).raw)
    return im

def v_17():
    im = Image.open(requests.get('https://sun9-62.userapi.com/impg/pAbtr5aotIWDLSXdulqY8J95GMOHz2_taHPPNw/n3fBH4R5QfY.jpg?size=609x141&quality=96&sign=c1a97f97e323c510bf792dbd9bb89dde&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-25.userapi.com/impg/Zpxa-jhzhaibOruqljDZREzSlj6v7H55aPLFbw/j0EVtsq1vRQ.jpg?size=561x214&quality=96&sign=a370e5219a06dba2249b133fc4440e2a&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-31.userapi.com/impg/la1rIFUp9P5yseia49l03aVwzrzYtRT-KLg04A/QVEu3X_5Loc.jpg?size=652x509&quality=96&sign=ce43cc5610bbd5be0231236171281e26&type=album', stream=True).raw)
    im4 = Image.open(requests.get('https://sun9-26.userapi.com/impg/wodEJY03eAOo6QHD9bno4leAEpV8dp5cdHlNDQ/qYrV4Gu9o-k.jpg?size=614x451&quality=96&sign=13b5883443514eaaa8b613120758c476&type=album', stream=True).raw)
    im5 = Image.open(requests.get('https://sun9-21.userapi.com/impg/nr4w3E40two8XzWYij6Q_KpLnCDi6Pxr9bK8Lw/vseHGz4SnPM.jpg?size=789x234&quality=96&sign=79c78c15ccc538a444ca7deb76d911c0&type=album', stream=True).raw)
    im6 = Image.open(requests.get('https://sun9-25.userapi.com/impg/dZYakR_YjVefq0Iq_6UBatEwVzczPmKRst-nCw/rCFa81m6Jjg.jpg?size=782x678&quality=96&sign=400fd87dd88a905e87005f9aadbe62f8&type=album', stream=True).raw)
    im7 = Image.open(requests.get('https://sun9-63.userapi.com/impg/d1_DSwg00pDzKtn99phS100w402lVitMjctNGw/tzAmJJNKWcE.jpg?size=497x438&quality=96&sign=2e5fce2135567bf7f8730c4a78ad59dd&type=album', stream=True).raw)
    return im, im2, im3, im4, im5, im6, im7

def v_18():
    im = Image.open(requests.get('https://sun9-7.userapi.com/impg/4-g-7AyJSPMA9SbcSK4A-B5nsQJNQ_DbqhkPjg/yYXeGGFSkaU.jpg?size=794x548&quality=96&sign=fa0761d840e918502fa564a58cd412cd&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-70.userapi.com/impg/yub1EWDeeP88yBJvBGjdeUeG3s5YB1nbTl12-w/4sPx621SN04.jpg?size=799x590&quality=96&sign=eb485e7bbe9cd3b0e86759362505b508&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-37.userapi.com/impg/CZtY_vH9BSNJUvlwa66roGvOlTUxlNNw1zFKAw/umgJ9aO0aes.jpg?size=788x59&quality=96&sign=24f3cbfc3658c5f0a64d5a44444f1e18&type=album', stream=True).raw)
    return im, im2, im3

def v_19():
    im = Image.open(requests.get('https://sun9-21.userapi.com/impg/H8ed6gLXQWuKfny4F6tY1h-ymvouT-9lJY78XQ/O-fwqpU9-k0.jpg?size=797x687&quality=96&sign=9acd2427876caa1bb42d2532ce3b8ade&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-31.userapi.com/impg/pQVeJrEXxMpYxhB46BOcgeLXPDDoDcXKTVZojQ/FYLkrEDFhDQ.jpg?size=818x606&quality=96&sign=ae2da953671d648f0dfa58868e6c9ea7&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-63.userapi.com/impg/8DB8hml4upGwXT5n_9aSwgwm7kBb7RYgShNlOA/cmfmvmPy70Q.jpg?size=779x563&quality=96&sign=9c30190046667ef973ef7cb037584579&type=album', stream=True).raw)
    im4 = Image.open(requests.get('https://sun9-12.userapi.com/impg/T3s1egS3n1L8JO_6MNBAdyitVLgOXFqN3b2gZg/Mp4mzYdr4L8.jpg?size=786x334&quality=96&sign=b70fa4e3a0c376d79acffbd46cd8a0b6&type=album', stream=True).raw)
    im5 = Image.open(requests.get('https://sun9-63.userapi.com/impg/AzAYlDXnq3FBDdiToC_U8A8RgfmJCj-MQWT5MQ/G3NgUY1Dhzw.jpg?size=805x756&quality=96&sign=c89d0c968c26cdb06516afa2f530d2f4&type=album', stream=True).raw)
    im6 = Image.open(requests.get('https://sun9-36.userapi.com/impg/CQSdKNPZTe3XGA4P5JN6q1uBxx7T7s0_7_ZBWw/ALCufi15KPo.jpg?size=776x255&quality=96&sign=7fe2db44a84c62e82276f7b50aee0617&type=album', stream=True).raw)
    im7 = Image.open(requests.get('https://sun9-33.userapi.com/impg/UM521QWlu_V2lZ3VuNhbcYZ1SNFApuQ7P7ciww/vc7lYzJ-gMA.jpg?size=793x718&quality=96&sign=f153581cdc3e5a90b201859b1a70e953&type=album', stream=True).raw)
    im8 = Image.open(requests.get('https://sun9-12.userapi.com/impg/eAmLd3lwlHE0rfeX8oWo7VvEfVHFF-mwNdyl2Q/UlskYzHX2lY.jpg?size=683x134&quality=96&sign=2374c5936d6164418157c87740650635&type=album', stream=True).raw)
    im9 = Image.open(requests.get('https://sun9-78.userapi.com/impg/j13Id961PrH8jr6LQyhplx_HaiAHWymu5mqyOQ/bcxbgJs6KE8.jpg?size=797x515&quality=96&sign=054eb54f694c240ba57c48a0ed339d4b&type=album', stream=True).raw)
    return im, im2, im3, im4, im5, im6, im7, im8, im9

def v_20():
    im = Image.open(requests.get('https://sun9-40.userapi.com/impg/EIYy90DJgYK9WZrzrY-eA0HUSHZwx2sAGT1VrQ/1XUJbdZTpUw.jpg?size=787x465&quality=96&sign=08cff4d362ab490eb27ec82ecc7467cd&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-35.userapi.com/impg/yfh5NnNKYdYbC7zZqOFeJrA4jVy09aT-KJHoXQ/uk2sAZuF0E8.jpg?size=675x711&quality=96&sign=d57490655a3af22391a3e3e7373a3b43&type=album', stream=True).raw)
    return im, im2

def v_21():
    im = Image.open(requests.get('https://sun9-20.userapi.com/impg/nD8DwwmuD5_MTfn9rZ9UEOBZITKFsClJB9pDEA/9rWTzVwtAZo.jpg?size=1340x730&quality=96&sign=c29df8d81cf283fd21deadb9b312dca9&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-59.userapi.com/impg/mRahYOFqB8V6X7TPA703pJuzKFnL9-2l637kgQ/NuKfDxtwnnI.jpg?size=1600x836&quality=96&sign=df8be0e35c546b8aa9e5d40802f36706&type=album', stream=True).raw)
    return im, im2

def v_22():
    im = Image.open(requests.get('https://sun9-30.userapi.com/impg/DSkqTflXPdDP2jmxVu9Yv5_v4Y-TENchsH1Klw/z-ON3B6VtpE.jpg?size=758x263&quality=96&sign=f9840f221b4ac3f651a82e76d208c600&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-73.userapi.com/impg/u_5WdWS3HwyTPrPQ34a5hCyaZDTCBYGfR7CY-g/SwmFg1GHW50.jpg?size=765x532&quality=96&sign=52dc6aeabd61411155db9dd1b2236de0&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-79.userapi.com/impg/6djjUmplaZxKZI9vjF9ddO5EbaEpxb6QOgcEzg/Ew33H4Tnb1U.jpg?size=746x192&quality=96&sign=f8daab2a8ffcb8a3edef9b2e37f57a82&type=album', stream=True).raw)
    return im, im2, im3

def v_23():
    im = Image.open(requests.get('https://sun9-59.userapi.com/impg/s6PjzGQiCgo31_oak0bbTUH2YZcFiSaPdGhpPQ/3m02Eziik14.jpg?size=714x218&quality=96&sign=e386b3ddf95c3fa8556b7f3bfe3386c9&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-74.userapi.com/impg/B666lLrgrWBoUkv_48ztsEuh1FBttEwYPnpcPg/WwkeeHP9zQs.jpg?size=760x652&quality=96&sign=1b697ab041b3e05eac28070fa4999927&type=album', stream=True).raw)
    return im, im2

def v_24():
    im = Image.open(requests.get('https://sun9-16.userapi.com/impg/dTVnJ2hu-spvN3nvad5SsdHBcKOpSd3bIDX0-w/v6T478uQKo0.jpg?size=1413x579&quality=96&sign=528a1d52d51b8091f1425d326fe7c06c&type=album', stream=True).raw)
    return im

def v_25():
    im = Image.open(requests.get('https://sun9-11.userapi.com/impg/VPz5stV1BLg2Y95hMqbTVAMgIvCQEZWklY0YaA/tFovZsgk9EA.jpg?size=700x654&quality=96&sign=b4e52f82801a1d0da4af71662a90ed97&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-19.userapi.com/impg/Xofu9n91JpXwfMO0qVFNYdjvHjAbRtISmF590g/gNza1jTDeI4.jpg?size=641x164&quality=96&sign=2fc4477eed2c9c98884a6da5d61133fa&type=album', stream=True).raw)
    return im, im2

def v_26():
    im = Image.open(requests.get('https://sun9-12.userapi.com/impg/k6tH1z-MPvYVNRhvIkzMsG70TCBlg_-X4DGOEQ/LtQ5vvineDk.jpg?size=1448x462&quality=96&sign=e6b42333099c301b4cae3953b967d532&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-19.userapi.com/impg/SiDym306dS7wqekh8ClKCJiqzk6DovJ7LBE_FQ/8TXCK1ZTjyk.jpg?size=1448x830&quality=96&sign=1e81455c9baf0064e2c969a4db5447ee&type=album', stream=True).raw)
    return im, im2

def v_27():
    im = Image.open(requests.get('https://sun9-15.userapi.com/impg/CNA-AAp0jH-rdCcahCcxDvvLb2V8gdkGjH6Vcw/1wwfqrdj-6Y.jpg?size=1448x830&quality=96&sign=62a3c50c1b781ca6bdb27a8946565c30&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-59.userapi.com/impg/PCWl4maxA99Q-l7ck0VccwY0MAjq10i9IuUV0Q/xjZfPBis03o.jpg?size=1448x900&quality=96&sign=96df00f850c15e97bede86f9015181df&type=album', stream=True).raw)
    return im, im2

def v_28():
    im = Image.open(requests.get('https://sun9-20.userapi.com/impg/LwJCmc-QVc_wPUOnBxFgG4UJFQMQBIleH-JhWA/ZYnJuKGDrgw.jpg?size=1448x900&quality=96&sign=dcd711ae2933c510d5403d1f5ffdd8fe&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-34.userapi.com/impg/UnYK02Y3q-l7GZqTIWpU1unZewjrzQtP-gu_tg/QzHfIB7mx5Y.jpg?size=1448x388&quality=96&sign=0fe4015a46e8328e787be1ccc983e2a2&type=album', stream=True).raw)
    return im, im2

def v_29():
    im = Image.open(requests.get('https://sun9-33.userapi.com/impg/PdwMq8txkS2EwaaRdEMpnagQjDhXH-vrZ-MRAw/dOGRgyVzxhE.jpg?size=1448x1294&quality=96&sign=51064e95498d42aea7e4048b8daeef9e&type=album', stream=True).raw)
    return im

def v_30():
    im = Image.open(requests.get('https://sun9-51.userapi.com/impg/uGJRBmLxBUNOL09cj5JtmfSmbdFMEzgvrcJ8jg/Gw_VsBQI1Ws.jpg?size=1448x1108&quality=96&sign=da81d60c54610586574a6251a6193d49&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-14.userapi.com/impg/LG5m6NZZqKm5DoK67ApM-3TvnTwSKV5733fz1Q/z67iOdEGy-0.jpg?size=1448x902&quality=96&sign=9fa4889cd69092c66479db11de2a8aeb&type=album', stream=True).raw)
    return im, im2

def v_31():
    im = Image.open(requests.get('https://sun9-15.userapi.com/impg/yZCGfyb8cWtYiQJemyMFElnufxhB69WKxaMdUQ/iLVgQKRv9kE.jpg?size=1278x1294&quality=96&sign=3eadda4b4804ad8cc1ce8a7be38b3cea&type=album', stream=True).raw)
    return im

def v_32():
    im = Image.open(requests.get('https://sun9-73.userapi.com/impg/l5Ms9cc8yuLzX2S_lQCoFOQuAg1cIVlfholf4w/v6xlJvBRDDs.jpg?size=1278x968&quality=96&sign=e56ada8a820c6624dfe28349745c48de&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-11.userapi.com/impg/kB4gLA5kteUzXZyV4G_tZzPrNagxZtsRC5ahJg/l0O_O7nz_0s.jpg?size=912x540&quality=96&sign=802fb7a237b6bf7af057703e19652518&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-57.userapi.com/impg/l9CxqddtJ8ZXHQDxtEzuFoNk0Es9bvoYp4BD4w/Xd7SaHJeG_8.jpg?size=912x770&quality=96&sign=bd5bd8caa8a967687c16ed62598007dc&type=album', stream=True).raw)
    im4 = Image.open(requests.get('https://sun9-77.userapi.com/impg/bZGaFP7tl5tL_Da6GuuhB9QV9wY8x-us32gYHA/mfptYFbR-_Y.jpg?size=912x770&quality=96&sign=5ca9da386c56d2fa38efb01a3836cc9c&type=album', stream=True).raw)
    im5 = Image.open(requests.get('https://sun9-17.userapi.com/impg/I1E4xe7jrlLVM392iAoNIezo3ZMwGSxaM3Me8Q/MPfAvP4vpAQ.jpg?size=912x1042&quality=96&sign=b318a1e947f33f77fbdbab0075695430&type=album', stream=True).raw)
    im6 = Image.open(requests.get('https://sun9-46.userapi.com/impg/46STDF-bFK8MSsCeQUEYjTxIC0Zo6tJADPaklw/7W89Uty0niU.jpg?size=912x436&quality=96&sign=09e00474c0e959d90f05271478336cda&type=album', stream=True).raw)
    im7 = Image.open(requests.get('https://sun1-22.userapi.com/impg/UeKsysw9__0Fvxr6NLwRqBHGHm8s5wlx5c74Aw/jLSrYGjcGXY.jpg?size=746x308&quality=96&sign=69e5fbeb31b6e0753e0991e6e2dd0a11&type=album', stream=True).raw)
    return im, im2, im3, im4, im5, im6, im7

def v_33():
    im = Image.open(requests.get('https://sun9-79.userapi.com/impg/OpV-ngqri5ZiAySEk2K6FwPMJpBjEFR5PE7P5A/_7Z6n7kvvzA.jpg?size=1256x1146&quality=96&sign=c311a25c03a70ab5beef311dd56da46b&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-9.userapi.com/impg/KF1AmiYUOQQktCn5qmYYev_rPfhSA3gcmffP1w/Tpq-iKQTkQs.jpg?size=1096x746&quality=96&sign=9db3901f0dd46d71e49ff2e13bfd39bf&type=album', stream=True).raw)
    return im, im2

def v_34():
    im = Image.open(requests.get('https://sun9-75.userapi.com/impg/hM51Yzv0bJ6gn9ct6YAlL1o3i9Y1EfIOKmSqJQ/k4cW6s18cIw.jpg?size=805x567&quality=96&sign=e4dd63ea7840c42919597e4e904d1bde&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-37.userapi.com/impg/NmO7Huu1XUJacEMygzwRmJW8Fx59XZ60EmQrTA/gW-0Ulw7Kzs.jpg?size=802x708&quality=96&sign=8458fa3e79939516d45fc23c2110421a&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-5.userapi.com/impg/XO0vsmxG5-KC5jZFFY5YOo-aGu1lK9kf4M_4Dg/nhgAtD4-QDo.jpg?size=809x395&quality=96&sign=0b2111d5219d98d4adbb6aa647a74d94&type=album', stream=True).raw)
    im4 = Image.open(requests.get('https://sun9-74.userapi.com/impg/YYav6OkBzj3_G5S6eH-JNDihMSNzC8MsLzINCg/BzCm19g6-DY.jpg?size=718x672&quality=96&sign=2124942b02d31e1c35c5410257f6cadd&type=album', stream=True).raw)
    return im, im2, im3, im4

def v_35():
    im = Image.open(requests.get('https://sun9-37.userapi.com/impg/1kAw-yRnS8Gb-QLbNsVu6Feodu7CCd1bX5QQ-A/qSrj7Naqb5s.jpg?size=791x198&quality=96&sign=b52d75bad9a328914e9bc4c3e3bf55fa&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-53.userapi.com/impg/d1rUia4ClR6StO4rqLEBOzQChPiaKt3jlfrmtQ/lj9REnWtRG4.jpg?size=684x735&quality=96&sign=0f37ad40eb58e9075f848d9f9ede48ef&type=album', stream=True).raw)
    return im, im2

def v_36():
    im = Image.open(requests.get('https://sun9-10.userapi.com/impg/Slfqt9fUBkAeAagyvods6b5OSnc8dUGJetjWmQ/V-veYrtR-Mo.jpg?size=812x600&quality=96&sign=93a5091399b0f9abd06d5f9a67ba1bda&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-75.userapi.com/impg/Sac1UsLvjWtOzJZKb-1gzxYJ5zegz9OskINbaA/qq61x4n-7cM.jpg?size=796x460&quality=96&sign=7e00a9fb26acf1fd87fec27c7c0caa18&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun1-87.userapi.com/impg/JlUs_NrvButlBpVDangankKzSJf-S_wkQuCjcA/H28BOBduJ7g.jpg?size=812x566&quality=96&sign=108c15f92dee238f068f6d14d337a760&type=album', stream=True).raw)
    return im, im2, im3

def v_37():
    im = Image.open(requests.get('https://sun9-75.userapi.com/impg/biJuEaQZzI51TJ3dITqTJrWdoubawnOxtBU8QQ/SwT5rj6LhNI.jpg?size=794x237&quality=96&sign=bfebe6646654cd754354e9cc8c3a96f4&type=album', stream=True).raw)
    return im

def v_38():
    im = Image.open(requests.get('https://sun9-9.userapi.com/impg/4_8jp5t-hz_HIDx9EEgHmMu_eq8BilFXXDgXWQ/OTqertpHfWw.jpg?size=792x522&quality=96&sign=1d1ef0e8901669d18eb00b36b756158f&type=album', stream=True).raw)
    return im

def v_39():
    im = Image.open(requests.get('https://sun9-27.userapi.com/impg/iA6iz_ZaY4uEivtuWFonbBzhel51qEhqivJ8sQ/DwVjeZ4xnTQ.jpg?size=790x348&quality=96&sign=28b9297f59595839e9ae7081bcde75c9&type=album', stream=True).raw)
    return im

def v_40():
    im = Image.open(requests.get('https://sun9-60.userapi.com/impg/uVpu2IDCI-mhzqO2-WUgfUQEa8xDa5JONeBLRg/C0Q14oSaZ-k.jpg?size=801x215&quality=96&sign=d9fcc24323d2024ab60d8412016260fc&type=album', stream=True).raw)
    return im

def v_41():
    im = Image.open(requests.get('https://sun9-10.userapi.com/impg/b5EK8syHFTFE3rgUH8hgLhw1Hh8v0sNCSqK6Cw/qFl3jrAuxz0.jpg?size=802x626&quality=96&sign=464f634f23143f3444aa985250def488&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-23.userapi.com/impg/LobNZoJytRKKLPAjv4zOQwB3YpfRP--n0mf7Dw/Hq9dfb4pxO8.jpg?size=770x317&quality=96&sign=23c5b35612d3bd7df9848ff3ec8ce2b0&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-49.userapi.com/impg/ymjcJJH-1chSLwj773glGz8pxXEn_pqUTIdj5A/KdRwuXEmKAU.jpg?size=809x669&quality=96&sign=7a5e955d0ec89e340455e7a4f57234ed&type=album', stream=True).raw)
    return im, im2, im3

def v_42():
    im = Image.open(requests.get('https://sun9-78.userapi.com/impg/2WtSYseQo3MKBeR3-90pnkiaGEtqNLcuGfPQDw/_NiFLWYrgBk.jpg?size=794x402&quality=96&sign=1d8a64e7c5436d67ab93db151a843de4&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-7.userapi.com/impg/L0mhNVMKC7a-l2_zsIfcv-hUnxAa9zAeDWWRwQ/KTdWOvO8GlY.jpg?size=798x694&quality=96&sign=e7253e84b5bfe25e32fbaab40fbe4602&type=album', stream=True).raw)
    return im, im2

def v_43():
    im = Image.open(requests.get('https://sun9-63.userapi.com/impg/nyd251xb2dvvODMmOKDB01iLM11XFSPWWFWZ0A/0nKU4TTN4uc.jpg?size=766x709&quality=96&sign=78844e70d268e90c6df1473d4f008acb&type=album', stream=True).raw)
    return im

def v_44():
    im = Image.open(requests.get('https://sun9-79.userapi.com/impg/Q7K74a4Ic_46o1Znq4tAZ4FYRPFM_QOGVTzg_Q/U8L9PvUETa8.jpg?size=755x247&quality=96&sign=b2589693544c6b77a08f9b3d32eb9094&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-24.userapi.com/impg/9v2Z3MQaZDMn1BeGk4VimMStw3CZTv3Kuj9jVQ/9RcGIGk_Yvk.jpg?size=791x429&quality=96&sign=5cef50e22d2f3258280d0235872f5986&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-24.userapi.com/impg/rF78dZkDZy7HGQeUV_HH1pSKKfQxDBlSbmEsRw/Bb_TcDDbM6w.jpg?size=802x567&quality=96&sign=602354353a822840aa3d0f95f6738f8f&type=album', stream=True).raw)
    return im, im2, im3

def v_45():
    im = Image.open(requests.get('https://sun9-47.userapi.com/impg/xITxrRvKvsygv4D74G8NItBJtKhZHe8nJpY5zA/Ib6DSErM8q4.jpg?size=786x460&quality=96&sign=859ae31bd8fb128e923f850b34b79bf8&type=album', stream=True).raw)
    return im

def v_46():
    im = Image.open(requests.get('https://sun9-20.userapi.com/impg/91v-xBVXx8ThkT5bewvIJuW26RRMEThM2FpXvw/Z_dVnB6eQIk.jpg?size=788x201&quality=96&sign=045cd13b7206a93ef20da4de874c4e55&type=album', stream=True).raw)
    return im

def v_47():
    im = Image.open(requests.get('https://sun9-58.userapi.com/impg/Hasuksbjuw911QcaP1KoSe5JXBN3LVJcohn8pg/mizrpP1pnTw.jpg?size=757x135&quality=96&sign=4cce6b13a8e6a7bc61ea3538eee87d4b&type=album', stream=True).raw)
    return im

def v_48():
    im = Image.open(requests.get('https://sun9-45.userapi.com/impg/YOc6L4Qfe6F2Ao9yBnqPqvtxcELk_kQhDFI56A/2mA3dVetDFs.jpg?size=465x509&quality=96&sign=d8a3422be99742d201fc83268c5418cc&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-9.userapi.com/impg/5KrHRqNvklMHmYjApx8CZoaSZGufq1fGo7JvCg/uV7ccihMzZs.jpg?size=382x446&quality=96&sign=f1cbe5d0c6977589bf245345c454683a&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-39.userapi.com/impg/3B2NoERJUKTT_TfII1YQQZCbX8tRi-TbNKM5-w/55SaieXf8LE.jpg?size=422x677&quality=96&sign=ca11cfa7d544ef625bcb4bbac46b840a&type=album', stream=True).raw)
    im4 = Image.open(requests.get('https://sun9-50.userapi.com/impg/-0B_crrXcwL3hwqrTvD6O3eBU0YVvnqvOYVELA/GnQ3ZF2_i-8.jpg?size=543x417&quality=96&sign=ce53078e8e2ef734e76ffcfcf9e5a63b&type=album', stream=True).raw)
    im5 = Image.open(requests.get('https://sun9-50.userapi.com/impg/N0Hmf5tN3WiD5xTjkvG0PjQY2hDMKzze3cZAQg/rKIkz9Ab92o.jpg?size=500x295&quality=96&sign=7f231bef6e40f369d7eda8eedfb4eb17&type=album', stream=True).raw)
    return im, im2, im3, im4, im5

def v_49():
    im = Image.open(requests.get('https://sun9-35.userapi.com/impg/4HcPfwMC4p2nqsIw_6iCnFc3HnLwdvLdSHK2Ig/FeLMXwcI57U.jpg?size=766x655&quality=96&sign=5507d4734c063b2615df1fb262c6f9ad&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-16.userapi.com/impg/3xUXZA4xg8OD7R1hm00NtnpOYpKNEk7uqh5QPw/Qv_f4sKpObc.jpg?size=757x633&quality=96&sign=a51afad2e18ea20043f06fcf1c6cb188&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-30.userapi.com/impg/NPcG686RHlvdTM-wpgwnbTp0ktpIAELHNZDrOg/XY3ytP-v5IA.jpg?size=771x574&quality=96&sign=919f2e22e8e03381ec130bef50f23ab8&type=album', stream=True).raw)
    im4 = Image.open(requests.get('https://sun9-46.userapi.com/impg/4DvseSwFPsPZTuPeMd6eylC33Ks80betWNlJmg/6Ri1PF5l3NQ.jpg?size=734x421&quality=96&sign=ffcd5e417fc28f01d55a8c27acdea558&type=album', stream=True).raw)
    return im, im2, im3, im4

def v_50():
    im = Image.open(requests.get('https://sun9-66.userapi.com/impg/tt7F3Y00oP7Qyq9yipC-KsG27_t82oyIohxSFA/e4ifb9t0sGE.jpg?size=756x672&quality=96&sign=0e3a2933be445b288d3bb1af79fd8a69&type=album', stream=True).raw)
    im2 = Image.open(requests.get('https://sun9-28.userapi.com/impg/HRefjb_giQb35C2tWU0axK4eUjKzisaVMBMDow/-zEB8bx5Iek.jpg?size=765x633&quality=96&sign=757279ddad0b17559c07c1f17c57f933&type=album', stream=True).raw)
    im3 = Image.open(requests.get('https://sun9-59.userapi.com/impg/55cPVwnhPiA8pqgyu6yVS00snKj0Qa0nP8KzYg/R3I5j-LQuxI.jpg?size=763x578&quality=96&sign=ac05e6d78e2dc86d3d5bcf06b760c573&type=album', stream=True).raw)
    return im, im2, im3