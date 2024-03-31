--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: article; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.article (
    id uuid NOT NULL,
    event_id uuid NOT NULL,
    title character varying NOT NULL,
    text character varying NOT NULL
);


ALTER TABLE public.article OWNER TO postgres;

--
-- Name: country; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.country (
    id uuid NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.country OWNER TO postgres;

--
-- Name: document; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.document (
    id uuid NOT NULL,
    event_id uuid NOT NULL,
    file character varying,
    name character varying NOT NULL
);


ALTER TABLE public.document OWNER TO postgres;

--
-- Name: event; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.event (
    id uuid NOT NULL,
    title character varying NOT NULL,
    about character varying NOT NULL,
    banner character varying,
    registration_start timestamp with time zone NOT NULL,
    registration_end timestamp with time zone NOT NULL,
    participation_start timestamp with time zone NOT NULL,
    participation_end timestamp with time zone NOT NULL,
    place_id uuid NOT NULL,
    target_group_id uuid NOT NULL,
    author_id uuid NOT NULL,
    sport_type_id uuid NOT NULL
);


ALTER TABLE public.event OWNER TO postgres;

--
-- Name: place; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.place (
    id uuid NOT NULL,
    country_id uuid NOT NULL,
    address character varying NOT NULL
);


ALTER TABLE public.place OWNER TO postgres;

--
-- Name: social_link; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.social_link (
    id uuid NOT NULL,
    event_id uuid NOT NULL,
    link character varying NOT NULL
);


ALTER TABLE public.social_link OWNER TO postgres;

--
-- Name: sport_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sport_type (
    id uuid NOT NULL,
    name character varying NOT NULL,
    description character varying NOT NULL
);


ALTER TABLE public.sport_type OWNER TO postgres;

--
-- Name: starter_item; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.starter_item (
    id uuid NOT NULL,
    event_id uuid NOT NULL,
    starter_item character varying NOT NULL
);


ALTER TABLE public.starter_item OWNER TO postgres;

--
-- Name: target_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.target_group (
    id uuid NOT NULL,
    gender character varying NOT NULL,
    minimal_age integer NOT NULL
);


ALTER TABLE public.target_group OWNER TO postgres;

--
-- Name: ticket; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket (
    id uuid NOT NULL,
    event_id uuid NOT NULL,
    title character varying NOT NULL,
    extra_title character varying NOT NULL,
    price integer,
    max_places integer NOT NULL,
    sport_type_id uuid NOT NULL
);


ALTER TABLE public.ticket OWNER TO postgres;

--
-- Name: ticket_registation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket_registation (
    id uuid NOT NULL,
    ticket_id uuid NOT NULL,
    user_id uuid NOT NULL,
    serial_number integer NOT NULL
);


ALTER TABLE public.ticket_registation OWNER TO postgres;

--
-- Data for Name: article; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.article (id, event_id, title, text) FROM stdin;
fbfa5c52-3da2-4262-9f0e-bfce856a0876	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Дистанции	<ul>\n<li>\nЭтап кубка России по триатлону Средняя дистанция – 1,9 км плавание, 90 км велогонка, 21,1 км бег\n</li>\n<li>\nЧемпионат Любителей по триатлону Средняя дистанция – 1,9 км плавание, 90 км велогонка, 21,1 км бег\n</li>\n</ul>
cc118d35-a39c-4aaa-8432-5b39b1c67559	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Награждение	Атлеты награждаются денежными призами, подарками организаторов и партнеров в соответствии с регламентом соревнований.
f653679e-ee98-4da9-9d1b-9b30797ea632	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Схемы дистанции	 <img src="https://rrweb.russiarunning.com/-x-/generalimages/06892590-27e6-495d-ab3a-a125261fb4ef.jpg" loading="lazy" max-width="100%" alt="No image(" >
22051f2e-78bf-4c30-9499-4785790fd7c2	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Этапы	<h4>Плавательный этап:</h4>\n<p>\nПлавательный этап гонки будет проводиться в акватории Амурского залива. Атлетам необходимо будет преодолеть выбранную дистанцию в чистой морской воде Японского моря.\nГидрокостюмы разрешены.\n</p>\n\n<h4>Велосипедный этап:</h4>\n<p>\nВелоэтап гонки пройдёт по Федеральной трассе от полуострова Де-Фриз в сторону поселка Шмидтовка, с качественным дорожным покрытием и незначительным перепадом высот.\nРазделочные велосипеды разрешены, драфтинг - запрещен.\n</p>\n\n<h4>Беговой этап:</h4>\n<p>\nБеговой этап соревнований пройдет по уникальному низководному мосту, соединяющему полуостров Де-Фриз с районом города Владивостока – Седанка. Впервые этот мост будет открыт для проведения соревнований. Участники средней дистанции преодолеют три круга, протяжённостью 21,1 км. над морской гладью Амурского залива. Перепад высот отсутствует.\n</p>
ac9f1b86-15fb-442c-9ce3-82a61389213e	bac8e7df-88f5-4da0-bf3e-f26850c132c1	Место проведения	<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/org/russkaya_lyzhnya/44216590496/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Русская лыжня</a><a href="https://yandex.ru/maps/11409/primorsky-krai/category/sports_base/184107295/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:14px;">Спортивная база в Приморском крае</a><iframe src="https://yandex.ru/map-widget/v1/?ll=131.853927%2C43.058075&mode=poi&poi%5Bpoint%5D=131.854937%2C43.057646&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D44216590496&z=16.63" width="99%" height="400" loading="lazy" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>
bf68a4b2-22bc-4eab-ad06-4901911214e6	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Место проведения	<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/11409/primorsky-krai/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Приморский край</a><a href="https://yandex.ru/maps/11409/primorsky-krai/house/posyolok_de_friz_32/ZUoHaA5oTkMGWEJuYGJzdnhhbQs=/?ll=131.991428%2C43.274450&utm_medium=mapframe&utm_source=maps&z=15.8" style="color:#eee;font-size:12px;position:absolute;top:14px;">Яндекс Карты</a><iframe src="https://yandex.ru/map-widget/v1/?ll=131.991428%2C43.274450&mode=whatshere&whatshere%5Bpoint%5D=131.987614%2C43.274293&whatshere%5Bzoom%5D=17&z=15.8" width="99%" height="400" frameborder="1" loading="lazy" allowfullscreen="true" style="position:relative;"></iframe></div>
5500632c-b80b-40e9-abbf-22711824d88e	bac8e7df-88f5-4da0-bf3e-f26850c132c1	Схемы дистанции	<p>Определяются колличеством кругов по следующему маршруту</p>\n<img src="https://orgeo.ru/files/event/banner_top/32530_o.jpg?t=" alt="No image(" max-width="100%" loading="lazy">
ec9db6c3-9ed0-4574-a38c-a1e0e2c0b5af	bac8e7df-88f5-4da0-bf3e-f26850c132c1	Программа	<p>\n<b>9:45</b>         Открытие мероприятия\n</p>\n<p>\n<b>10:00</b>        Старт марафона\n</p>\n<p>\n<b>10:15 - 15:30</b>   Прохождение трассы\n</p>\n<p>\n<b>16:00</b>        Финиш первых участников\n</p>\n<p>\n<b>16:30</b>        Награждение победителей\n</p>\n<p>\n<b>17:30</b>        Время для общения, фотосессии\n</p>\n<p>\n<b>19:00</b>        Завершение мероприятия\n</p>\n<p>Время мероприятия может подвергаться изменениям в зависимости от условий и обстоятельств.</p>
d7a9cab9-d4a1-4f60-9cb5-37ba0f9180fc	bac8e7df-88f5-4da0-bf3e-f26850c132c1	Безопасность	<ul>\n<li>\nНа всей протяженности трассы будут размещены медицинские\n</li>\n<li>\nВсе участники должны носить защитные шлемы в течение всего марафона\n</li>\n</ul>
448a84e0-d6e5-4987-a3bb-83bb5fea6e76	60f83852-df72-4110-b27e-d1d3b65dcca2	Место проведения	<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/org/detskiy_ozdorovitelny_lager_nadezhda/29109097741/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Детский Оздоровительный Лагерь Надежда</a><a href="https://yandex.ru/maps/11409/primorsky-krai/category/resort/184106400/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:14px;">База, дом отдыха в Приморском крае</a><iframe src="https://yandex.ru/map-widget/v1/org/detskiy_ozdorovitelny_lager_nadezhda/29109097741/?ll=131.838705%2C43.728838&z=10" width="99%" height="400" loadig="lazy" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>
a7d32de4-fbb3-48f5-b929-7ca313bc7323	60f83852-df72-4110-b27e-d1d3b65dcca2	Этапы	<h4>Старт и разогрев</h4>\n<p>Участники собираются на старте, проводят разминку и получают последние инструкции от организаторов.</p>\n\n</h4>Трейлраннинг в лесу</4h>\n<p>Первый этап включает в себя бег через плотные леса, где участники преодолевают естественные преграды, такие как корни деревьев и неровности рельефа.</p>\n\n<h4>Пересечение реки</h4>\n<p>Участники сталкиваются с водным вызовом, пересекая реку. Это может включать в себя брожение через мелководье или преодоление реки по специальному мосту.</p>\n\n<h4>Подъем на возвышенность</h4>\n<p>Гонка включает в себя подъем на возвышенность с великолепными видами на окружающую местность, требующий участников использовать свою выносливость.</p>\n\n<h4>Секция скайраннинга</h4>\n<p>Этот этап включает в себя небольшой участок скайраннинга, где участники преодолевают крутые склоны или преодолевают естественные препятствия.</p>\n\n<h4>Спуск с возвышенности</h4>\n<p>После подъема следует захватывающий спуск с возвышенности, где участники должны проявить ловкость и технику для безопасного спуска.</p>\n\n<h4>Финиш</h4>\n<p>Гонка завершается на финишной черте, где участников встречают организаторы и зрители. После финиша предусмотрено время для отдыха, обмена впечатлениями и награждения победителей.</p>
16a310ae-5c82-4ca0-b163-7267aef3c5cc	60f83852-df72-4110-b27e-d1d3b65dcca2	Награждение	На церемонии награждения главное внимание уделяется победителям всех видов гонки. \nМы подчеркиваем что "на Уссури-Трейл мало не покажется никому" и ценят достижения на всех дистанциях
ec3bb3c0-4e53-4d6f-bc86-a932c294cd29	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Место проведения	<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/org/alyye_parusa/240340587540/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Алые паруса</a><a href="https://yandex.ru/maps/11409/primorsky-krai/category/yacht_club/184107279/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:14px;">Яхт-клуб в Приморском крае</a><a href="https://yandex.ru/maps/11409/primorsky-krai/category/bike_rental/9933541986/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:28px;">Прокат велосипедов в Приморском крае</a><iframe src="https://yandex.ru/map-widget/v1/?ll=131.870431%2C43.016980&mode=poi&poi%5Bpoint%5D=131.869093%2C43.017504&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D240340587540&z=16.7" width="99%" loading="lazy" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>
5e339666-1234-4c63-9423-a45f907d6e0d	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Безопасность	<b>Обязательно берите с собой средства связи</b>, для непредвиденных ситуаций. \nНа стартовой точке будет дежурить группа экстренной медицинской помощи и спасательная бригада.
feec0c82-b252-45c2-b711-ed5d87417e1f	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Программа	<p><b>09:00</b> \tОткрытие стартово-финишного городка, начало выдачи стартовых пакетов</p>\n<p><b>10:00</b> \tТоржественное открытие "Тутаевского полумарафона "Май.Мир.Молодость."</p>\n<p><b>10:05</b>  \tСтарт детского забега на 300 м</p>\n<p><b>10:08</b>  \tСтарт забега безграничных возможностей на 600 м</p>\n<p><b>10:16</b>  \tСтарт детского забега на 600 м</p>\n<p><b>10:28</b>  \tРазминка для участников дистанции 3 км</p>\n<p><b>10:40</b>  \tСтарт дистанции 3 км</p>\n<p><b>10:43</b>  \tНаграждение победителей забегов на 300м, 600 м, забега безграничных возможностей</p>\n<p><b>11:05</b>  \tНаграждение победителей дистанции 3 км</p>\n<p><b>11:17</b>  \tРазминка для участников дистанций 10 км и 21,1 км</p>\n<p><b>11:30</b>  \tСтарт дистанции 10 км</p>\n<p><b>11:35</b>  \tСтарт дистанции 21,1 км</p>\n<p><b>12:20</b>  \tНаграждение победителей дистанции 10 км в абсолютном зачете</p>\n<p><b>13:10</b>  \tНаграждение победителей дистанции 10 км по категориям</p>\n<p><b>13:20</b>  \tНаграждение победителей дистанции 21,1 км в абсолютном зачете</p>\n<p><b>14:15</b>  \tНаграждение победителей дистанции 21,1 км по категориям</p>\n<p><b>14:45</b>  \tОкончание бегового события</p>
3e26d8ca-8020-4f41-ad03-a0939c24ad0a	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Этапы	<ul>\n<li>\n<b>07:00</b> – Приготовление: Участники собираются на стартовой площадке, где проходит регистрация и выдача карт с указанием начальных координат контрольных точек. Команды подготавливают свою экипировку, строят стратегию и обсуждают план действий.\n</li>\n<li>\n<b>08:00</b> – Стартовый момент: Первый сигнал, и команды начинают своё движение\n</li>\n<li>\n<b>18:00</b> – Финиш: Команды представляют свои результаты, и те, кто прошел через все испытания успешно, получают заслуженные награды.\n</li>\n<li>\n<b>18:30</b> – Лучшие команды и участники, продемонстрировавшие выдающиеся спортивные достижения, получают награды и признание за свой вклад в зимний рогейн.\n</li>\n</ul>
\.


--
-- Data for Name: country; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.country (id, name) FROM stdin;
cdac8660-86e0-49c0-9588-d7e63691d93f	Владивосток
913842fe-39a3-4496-be47-270236bdc30a	Russia
\.


--
-- Data for Name: document; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.document (id, event_id, file, name) FROM stdin;
ef6d0467-aa45-4662-a06c-1a40b136e1d3	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	https://russiarunning.com/file/a6f3abbb-6045-468e-a9cc-be3484c1cee2/%D0%9F%D0%BE%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%A7%D0%9F%D0%9A%20%E2%84%96%20767%20%D0%94%D0%B5-%D0%A4%D1%80%D0%B8%D0%B7%202023%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B0%D0%BD.pdf/download	Положение о соревновании
7d8f5847-0c77-4e1c-b843-a7edc9047dbe	b37d9fff-680c-4285-a2bf-740c8b8c54b4	https://drive.google.com/file/d/17mxLJegam_NdZcAPl8fBQIp2MYbq0Zk9/view?usp=sharing	Инструкция
fcc1bf4a-0170-4f8c-bacc-d6c6cdca6985	60f83852-df72-4110-b27e-d1d3b65dcca2	https://orgeo.ru/files/event/file/30091_634b574074.doc	Положение о соревновании
ef072801-0033-4c25-a255-34d10bc0bc50	bac8e7df-88f5-4da0-bf3e-f26850c132c1	https://orgeo.ru/files/event/polozhenie/15360_polozhenie.doc	Положение о соревновании
\.


--
-- Data for Name: event; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.event (id, title, about, banner, registration_start, registration_end, participation_start, participation_end, place_id, target_group_id, author_id, sport_type_id) FROM stdin;
b37d9fff-680c-4285-a2bf-740c8b8c54b4	Зимний рогейн. Первый этап Кубка "Рогейн-ДВ"	"Зимний рогейн. Первый этап Кубка "Рогейн-ДВ" – захватывающее приключение, олицетворяющее встречу зимней природы, навигации и физической выносливости. Участники этого мероприятия сражаются в поиске контрольных точек, тщательно скрытых среди заснеженных ландшафтов. Спортсмены подвергают свою физическую выносливость, мастерство навигации в зимних условиях и стратегическое мышление серьезным испытаниям.\nКаждая команда сталкивается с уникальными вызовами, требующими не только ловкости и силы, но и стратегического мышления. Участники развивают искусство быстрого перемещения по разнообразным маршрутам, преодолевают снежные препятствия и преодолевают расстояния, чтобы успешно завершить этот зимний марафон.\nСоревнование способствует формированию командного духа и взаимопомощи, стимулируя спортсменов преодолевать трудности природы. Зимний рогейн – это возможность совместно с друзьями и командой преодолеть природные вызовы, создавая запоминающиеся моменты и насыщаясь энергией зимних приключений."	/src/assets/images/tempory-assets/rogey_banner.jpg	2023-12-31 14:00:00+00	2024-06-14 14:00:00+00	2024-06-30 14:00:00+00	2024-07-01 14:00:00+00	dab97643-665e-476b-93be-221b829b4dc1	39515764-58c0-401f-881d-46e976fb141d	8327c2db-770d-4c0a-8cc1-5bcfe9613ac4	2b029a3c-a3f8-4450-afbe-d05194a59ecd
49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Триатлон «Де-Фриз 113». Соревнования среди любителей и профессионалов.	<p>Главное событие по триатлону состоится во Владивостоке, в историческом месте, на полуострове Де-Фриз.</p>\n<p>\nГонка «Де-Фриз 113» уже во второй раз пройдёт по живописным местам пригорода Владивостока. Беговой участок будет проходить по Низководному мосту, который соединяет полуостров Де-Фриз с городом Владивосток.\n</p>\n<p>\nСпортивное событие проходит при поддержке Министерства физической культуры и спорта, Администрации Приморского края, Федераций триатлона России и Федераций триатлона Приморского края.\n</p>	/src/assets/images/tempory-assets/defize_banner.jpg	2023-12-31 14:00:00+00	2024-06-14 14:00:00+00	2024-06-30 14:00:00+00	2024-07-01 14:00:00+00	7915f50d-f387-4c85-bc7f-279967b93f35	39515764-58c0-401f-881d-46e976fb141d	76edff08-7def-402d-bca8-0ec70ab6d80b	2b029a3c-a3f8-4450-afbe-d05194a59ecd
60f83852-df72-4110-b27e-d1d3b65dcca2	Уссури-трейл.Осень	<p>\nСерия трейловых гонок "Уссури-трейл. Времена года-2024" представляет третий этап из четырех в Уссурийске. Это уникальное мероприятие, сочетающее бег, трейлраннинг, скайраннинг, атлетику и ходьбу, предлагает участникам неповторимый опыт взаимодействия с природой.\n</p>\n<p>\nОсенняя трасса прокладывает путь через дикую приморскую тайгу, предоставляя участникам возможность насладиться красочными видами, характерными для этого времени года. Плотные леса, живописные реки и возвышенности создают увлекательные вызовы для физической активности.\n</p>\n<p>\nВремена года добавляют свой неповторимый характер к каждой гонке, обогащая маршруты разноцветными листьями и особенными атмосферными условиями. Это соревнование не только ставит под сомнение физическую выносливость участников, но и вносит элементы приключения и взаимодействия с природой.\n</p>\n<p>\nМежрегиональные (зональные) соревнования способствуют обмену опытом между участниками из различных регионов, создавая дружественное сообщество людей, объединенных любовью к активному образу жизни и уважением к природе.\n</p>\n<p>\nЭто увлекательное событие, запланированное на осень, предлагает участникам не только физический вызов, но и возможность насладиться последними днями тепла перед наступлением зимы, создавая незабвенные воспоминания.\n</p>	/src/assets/images/tempory-assets/2_banner.jpg	2023-12-31 14:00:00+00	2024-10-03 14:00:00+00	2024-10-14 14:00:00+00	2024-10-16 14:00:00+00	698db308-6ac9-430e-8ec7-40f7747473de	39515764-58c0-401f-881d-46e976fb141d	76edff08-7def-402d-bca8-0ec70ab6d80b	b4917eef-8246-4feb-8eb5-b9eb818557d2
bac8e7df-88f5-4da0-bf3e-f26850c132c1	Традиционный веломарафон MTB XCM "Проба сил - 2024"	<p>\nВ воскресенье, 10 сентября, на Русском острове Владивостока пройдет третий веломарафон MTB XCM "Проба сил - 2024". Это стало традицией для местных велосипедистов собираться и участвовать в официальных соревнованиях по маунтинбайку. Участвовать планируют более 100 спортсменов из разных городов Приморья и Дальнего Востока, включая Хабаровск, Благовещенск и Биробиджан.\n</p>\n<p>\nМероприятие проводится на Русском острове, что добавляет природного очарования соревнованиям. Велосипедисты будут иметь возможность насладиться природой в ходе марафона.\n</p>\n<p>\nЭтот веломарафон становится важным событием для велосипедного сообщества региона, предоставляя участникам возможность проверить свои силы и поделиться опытом. Организаторы надеются, что мероприятие будет способствовать развитию велоспорта в регионе, создавая дружественную обстановку среди участников.\n</p>	/src/assets/images/tempory-assets/velik.jpg	2023-12-31 14:00:00+00	2024-08-19 14:00:00+00	2024-09-09 14:00:00+00	2024-09-09 14:00:00+00	5f364b0f-82a4-4e5e-b6ab-dd84b496d180	39515764-58c0-401f-881d-46e976fb141d	e6fc866f-c371-49d3-a11e-2dac2fa4a231	2b029a3c-a3f8-4450-afbe-b15194a59ecd
\.


--
-- Data for Name: place; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.place (id, country_id, address) FROM stdin;
7915f50d-f387-4c85-bc7f-279967b93f35	913842fe-39a3-4496-be47-270236bdc30a	г. Владивосток
5f364b0f-82a4-4e5e-b6ab-dd84b496d180	913842fe-39a3-4496-be47-270236bdc30a	г. Большой Камень
dab97643-665e-476b-93be-221b829b4dc1	913842fe-39a3-4496-be47-270236bdc30a	г. Уссурийск
7dc9372c-dacc-4f21-b86c-7613e1bcea56	913842fe-39a3-4496-be47-270236bdc30a	г. Находка
698db308-6ac9-430e-8ec7-40f7747473de	913842fe-39a3-4496-be47-270236bdc30a	г. Арсеньев
\.


--
-- Data for Name: social_link; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.social_link (id, event_id, link) FROM stdin;
c9170ff6-cea3-4a29-bee2-1f1c2b6783a5	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	https://vk.com
293e4d6d-3085-4cd4-9590-63f6ad5457df	bac8e7df-88f5-4da0-bf3e-f26850c132c1	https://vk.com
22e07d0e-e6a6-4e73-a74a-b98c3d3a4847	60f83852-df72-4110-b27e-d1d3b65dcca2	https://vk.com
b29c2f98-94cb-43da-a99e-c14b539aa476	b37d9fff-680c-4285-a2bf-740c8b8c54b4	https://vk.com
\.


--
-- Data for Name: sport_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sport_type (id, name, description) FROM stdin;
9d38f723-3e75-45ae-bd5b-205ebf24906d	Бег	foo
2b029a3c-a3f8-4450-afbe-d05194a59ecd	Триатлон	foo
09665761-6ead-4c40-b820-27ef4d4defb3	Лыжные гонки	foo
667dbad2-d2b6-4d52-b62c-5999837aa5e0	Плавание	foo
2b029a3c-a3f8-4450-afbe-b15194a59ecd	MTB марафон	foo
b4917eef-8246-4feb-8eb5-b9eb818557d2	Трейлраннинг	foo
077b509b-5331-4d05-8469-a8f2dfbf5474	Рогейн	foo
\.


--
-- Data for Name: starter_item; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.starter_item (id, event_id, starter_item) FROM stdin;
a4334582-a896-4171-a0bc-511891dad45d	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Плавательная шапочка
e353a57c-5ff9-452e-b81b-c48096182a44	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Стартовые Номера
1c13b4ff-5828-4629-ab88-e96d70e64889	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Чип для Индивидуального хронометража
023fc81d-3c69-441b-8c1a-74b9e9f7f390	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Наклейка для гардероба
0cf83550-a041-40af-a062-d4441e2ebeaf	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Вложения от партнеров
690a9a75-d026-4b38-923d-ee84544a9d41	bac8e7df-88f5-4da0-bf3e-f26850c132c1	Велосипед, подходящий для езды на пересеченной местности
2bd3dbee-170c-42c6-9295-f7602f63675e	bac8e7df-88f5-4da0-bf3e-f26850c132c1	Шлем
5c37ec34-4232-4712-925e-f4ca1099795e	60f83852-df72-4110-b27e-d1d3b65dcca2	Спортивная одежда и обувь
200a1756-9cc6-4822-a218-de27fd5140d2	60f83852-df72-4110-b27e-d1d3b65dcca2	Вода
297d4d57-759d-45e7-a434-9e58411fd530	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Аптечка
ed207a28-ab78-4d8f-a2ed-0c71387a5e52	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Комплект сменной сухой герметично упакованной одежды
628822ce-e870-4fc7-926c-07a2ed7a3cca	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Магнитный компас
94cd351b-d738-48c2-b4ab-cfb246d5c55a	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Запас питьевой воды и питания
e377c6a9-2414-48a7-bd13-adb9e2c142cc	60f83852-df72-4110-b27e-d1d3b65dcca2	Средства навигации
f5297116-cc5a-45c8-a617-a8bd4e6fa615	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Заряженный телефон
\.


--
-- Data for Name: target_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.target_group (id, gender, minimal_age) FROM stdin;
39515764-58c0-401f-881d-46e976fb141d	Любой	18
\.


--
-- Data for Name: ticket; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket (id, event_id, title, extra_title, price, max_places, sport_type_id) FROM stdin;
84da98e9-1c91-464d-8775-4bb0f9e6dc8b	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Этап Кубка России	113\nкм	50000	14	2b029a3c-a3f8-4450-afbe-d05194a59ecd
15fdef20-820b-4324-81a4-61c429ff7542	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Чемпионат Любителей	113\nкм	5000	30	2b029a3c-a3f8-4450-afbe-d05194a59ecd
2fd831e5-c79e-4e90-b75e-22aafef38588	bac8e7df-88f5-4da0-bf3e-f26850c132c1	Марафон	60\nкм	500	50	2b029a3c-a3f8-4450-afbe-b15194a59ecd
25fdef20-820b-4324-81a4-61c429ff7542	49a5d35a-e782-4a57-897e-fd8e52bf2ea8	Зритель	Зрите\nли	500	100	09665761-6ead-4c40-b820-27ef4d4defb3
2af6256c-01db-4567-abe9-155c8971b2ba	bac8e7df-88f5-4da0-bf3e-f26850c132c1	Зритель	Зрите\nли	0	100	2b029a3c-a3f8-4450-afbe-b15194a59ecd
98683d61-91b5-47a5-a0e4-5502af49d9fd	bac8e7df-88f5-4da0-bf3e-f26850c132c1	Полумарафон	30\nкм	500	50	2b029a3c-a3f8-4450-afbe-b15194a59ecd
a1f425d7-3d12-41fd-ad67-ecd9075aa4b1	60f83852-df72-4110-b27e-d1d3b65dcca2	BACKYARD20	20\nкм	0	100	b4917eef-8246-4feb-8eb5-b9eb818557d2
72d8da7c-7780-487f-b2f4-2194603a2335	60f83852-df72-4110-b27e-d1d3b65dcca2	BACKYARD13	13\nкм	0	100	b4917eef-8246-4feb-8eb5-b9eb818557d2
606c2ef2-d1f6-4e8b-973e-8f9789c26b2b	60f83852-df72-4110-b27e-d1d3b65dcca2	BACKYARD6	6\nкм	0	100	b4917eef-8246-4feb-8eb5-b9eb818557d2
7efe81d7-7d2f-4d6c-a2bc-d893226f7e99	60f83852-df72-4110-b27e-d1d3b65dcca2	Зритель	Зрите\nли	0	100	b4917eef-8246-4feb-8eb5-b9eb818557d2
200a636e-c8bc-4841-aabc-f3712f00edd3	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Группа НЕБЕГ	НЕ\nБЕГ	2000	30	077b509b-5331-4d05-8469-a8f2dfbf5474
578eb61a-dd5b-4d3b-ae84-f49bd6b2736c	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Зритель	Зрите\nли	0	100	077b509b-5331-4d05-8469-a8f2dfbf5474
99805fe1-a77e-4c49-b11d-62dec6fab427	b37d9fff-680c-4285-a2bf-740c8b8c54b4	Группа ПРОФИ	ПРО\nФИ	2000	30	077b509b-5331-4d05-8469-a8f2dfbf5474
\.


--
-- Data for Name: ticket_registation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket_registation (id, ticket_id, user_id, serial_number) FROM stdin;
6f90cbdc-3526-46ae-8eda-74fa8a76f3af	7efe81d7-7d2f-4d6c-a2bc-d893226f7e99	460f602b-cd8a-419e-9281-7f1d77f92824	1
3cbdfcbf-374f-438a-b39a-7999d913eb17	a1f425d7-3d12-41fd-ad67-ecd9075aa4b1	490048ec-8181-4c44-ac2a-e30d03c3c4c3	1
e302dfa2-55f6-4f6b-8a86-bf8f43b57e7e	200a636e-c8bc-4841-aabc-f3712f00edd3	490048ec-8181-4c44-ac2a-e30d03c3c4c3	1
258ec888-8e72-4e95-9d4e-698f6ae5abb3	84da98e9-1c91-464d-8775-4bb0f9e6dc8b	490048ec-8181-4c44-ac2a-e30d03c3c4c3	1
84c79623-a6bb-4927-9c1b-080e85e17d31	99805fe1-a77e-4c49-b11d-62dec6fab427	490048ec-8181-4c44-ac2a-e30d03c3c4c3	1
3b7fda1d-5c62-4903-b529-3e0ebbc62a78	98683d61-91b5-47a5-a0e4-5502af49d9fd	460f602b-cd8a-419e-9281-7f1d77f92824	1
7367cb16-9e99-40b7-9069-63d4143eedcf	200a636e-c8bc-4841-aabc-f3712f00edd3	460f602b-cd8a-419e-9281-7f1d77f92824	1
f603b90f-63b9-41cf-9e87-36000f00faed	606c2ef2-d1f6-4e8b-973e-8f9789c26b2b	460f602b-cd8a-419e-9281-7f1d77f92824	1
94f0d401-df74-4382-ac2e-230d56f5781e	72d8da7c-7780-487f-b2f4-2194603a2335	10b5b03d-4956-4724-8e76-23f885ffa166	1
c040ea8a-9d6d-4d1f-b856-73177cf3fc9a	99805fe1-a77e-4c49-b11d-62dec6fab427	10b5b03d-4956-4724-8e76-23f885ffa166	1
87c4aa71-9e6f-4e55-93c1-65805e111201	2fd831e5-c79e-4e90-b75e-22aafef38588	460f602b-cd8a-419e-9281-7f1d77f92824	1
097360a0-676a-4f1b-a0c2-0b457057fe57	15fdef20-820b-4324-81a4-61c429ff7542	460f602b-cd8a-419e-9281-7f1d77f92824	1
72581dfd-6daf-4bef-bb9c-8f08210c69d5	2af6256c-01db-4567-abe9-155c8971b2ba	c1bcf7fa-4c1c-40a8-9c25-44b9690b513b	1
0889cd72-1f4b-4cff-84d0-95f2f734492b	25fdef20-820b-4324-81a4-61c429ff7542	c1bcf7fa-4c1c-40a8-9c25-44b9690b513b	1
8f7f7a49-70ed-4864-b277-175d48660cd8	578eb61a-dd5b-4d3b-ae84-f49bd6b2736c	c1bcf7fa-4c1c-40a8-9c25-44b9690b513b	1
250cb5b4-f385-44ed-af00-bfd51f37e874	7efe81d7-7d2f-4d6c-a2bc-d893226f7e99	c1bcf7fa-4c1c-40a8-9c25-44b9690b513b	1
921d07f4-c258-412f-9141-94fe9b949f81	606c2ef2-d1f6-4e8b-973e-8f9789c26b2b	5951b8cc-3827-41bd-8394-a205001e4ca4	1
048d30a7-3724-4a8f-9ea5-9165615c1898	2fd831e5-c79e-4e90-b75e-22aafef38588	5951b8cc-3827-41bd-8394-a205001e4ca4	1
519200b1-71ab-4ba0-9441-97fd1fe95f59	84da98e9-1c91-464d-8775-4bb0f9e6dc8b	5951b8cc-3827-41bd-8394-a205001e4ca4	1
6fb23dfd-ecaa-43bf-b8c7-c6c9e27e02ee	200a636e-c8bc-4841-aabc-f3712f00edd3	5951b8cc-3827-41bd-8394-a205001e4ca4	1
c57e75a7-77d6-4bf9-b0b7-6bfc93cc6fc1	99805fe1-a77e-4c49-b11d-62dec6fab427	284d13e9-0aed-4510-b39a-dd3ae0dff8bc	1
03341125-2d6e-4ede-b169-f5e11e2e2db5	a1f425d7-3d12-41fd-ad67-ecd9075aa4b1	284d13e9-0aed-4510-b39a-dd3ae0dff8bc	1
00bd1320-c004-4de3-9ddf-6ac1fc24ed96	15fdef20-820b-4324-81a4-61c429ff7542	284d13e9-0aed-4510-b39a-dd3ae0dff8bc	1
117d5527-6f9e-4382-b93a-167b2c006931	98683d61-91b5-47a5-a0e4-5502af49d9fd	284d13e9-0aed-4510-b39a-dd3ae0dff8bc	1
6c6fbcec-5d90-4612-bc97-2b36df0e0a4a	25fdef20-820b-4324-81a4-61c429ff7542	344efecd-6466-4ccc-84fd-994b84c79a9e	1
d1cf6191-84eb-488c-bb84-c62474ad1fbf	2af6256c-01db-4567-abe9-155c8971b2ba	344efecd-6466-4ccc-84fd-994b84c79a9e	1
6770d100-338a-4812-9055-b1d8aa81cbfb	578eb61a-dd5b-4d3b-ae84-f49bd6b2736c	344efecd-6466-4ccc-84fd-994b84c79a9e	1
4a109be2-64f0-4943-9a40-6a26db03c46e	7efe81d7-7d2f-4d6c-a2bc-d893226f7e99	344efecd-6466-4ccc-84fd-994b84c79a9e	1
\.


--
-- Name: article articles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.article
    ADD CONSTRAINT articles_pkey PRIMARY KEY (id);


--
-- Name: country country_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_name_key UNIQUE (name);


--
-- Name: country country_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_pkey PRIMARY KEY (id);


--
-- Name: document document_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document
    ADD CONSTRAINT document_pkey PRIMARY KEY (id);


--
-- Name: event event_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_pkey PRIMARY KEY (id);


--
-- Name: place place_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.place
    ADD CONSTRAINT place_pkey PRIMARY KEY (id);


--
-- Name: social_link social_link_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.social_link
    ADD CONSTRAINT social_link_pkey PRIMARY KEY (id);


--
-- Name: sport_type sport_type_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sport_type
    ADD CONSTRAINT sport_type_name_key UNIQUE (name);


--
-- Name: sport_type sport_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sport_type
    ADD CONSTRAINT sport_type_pkey PRIMARY KEY (id);


--
-- Name: starter_item starter_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starter_item
    ADD CONSTRAINT starter_items_pkey PRIMARY KEY (id);


--
-- Name: target_group target_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.target_group
    ADD CONSTRAINT target_group_pkey PRIMARY KEY (id);


--
-- Name: ticket ticket_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket
    ADD CONSTRAINT ticket_pkey PRIMARY KEY (id);


--
-- Name: ticket_registation ticket_registation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_registation
    ADD CONSTRAINT ticket_registation_pkey PRIMARY KEY (id);


--
-- Name: article articles_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.article
    ADD CONSTRAINT articles_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.event(id);


--
-- Name: document document_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document
    ADD CONSTRAINT document_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.event(id);


--
-- Name: event event_place_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_place_id_fkey FOREIGN KEY (place_id) REFERENCES public.place(id);


--
-- Name: event event_sport_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_sport_type_id_fkey FOREIGN KEY (sport_type_id) REFERENCES public.sport_type(id);


--
-- Name: event event_target_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_target_group_id_fkey FOREIGN KEY (target_group_id) REFERENCES public.target_group(id);


--
-- Name: place place_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.place
    ADD CONSTRAINT place_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.country(id);


--
-- Name: social_link social_link_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.social_link
    ADD CONSTRAINT social_link_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.event(id);


--
-- Name: starter_item starter_items_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starter_item
    ADD CONSTRAINT starter_items_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.event(id);


--
-- Name: ticket ticket_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket
    ADD CONSTRAINT ticket_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.event(id);


--
-- Name: ticket_registation ticket_registation_ticket_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_registation
    ADD CONSTRAINT ticket_registation_ticket_id_fkey FOREIGN KEY (ticket_id) REFERENCES public.ticket(id);


--
-- Name: ticket ticket_sport_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket
    ADD CONSTRAINT ticket_sport_type_id_fkey FOREIGN KEY (sport_type_id) REFERENCES public.sport_type(id);


--
-- PostgreSQL database dump complete
--

