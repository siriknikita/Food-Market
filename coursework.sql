CREATE DATABASE market;
USE market;

SELECT * FROM market.orders;

CREATE TABLE IF NOT EXISTS user (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS food_products (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    category_id INT,
    price DECIMAL(10 , 2 ),
    image_url VARCHAR(255),
    FOREIGN KEY (category_id)
        REFERENCES categories (id)
);

CREATE TABLE IF NOT EXISTS beverages (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    category_id INT,
    price DECIMAL(10 , 2 ),
    image_url VARCHAR(255),
    FOREIGN KEY (category_id)
        REFERENCES categories (id)
);

CREATE TABLE IF NOT EXISTS baby_products (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    category_id INT,
    price DECIMAL(10 , 2 ),
    image_url VARCHAR(255),
    FOREIGN KEY (category_id)
        REFERENCES categories (id)
);

CREATE TABLE IF NOT EXISTS pet_products (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    category_id INT,
    price DECIMAL(10 , 2 ),
    image_url VARCHAR(255),
    FOREIGN KEY (category_id)
        REFERENCES categories (id)
);

CREATE TABLE IF NOT EXISTS snacks (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    category_id INT,
    price DECIMAL(10 , 2 ),
    image_url VARCHAR(255),
    FOREIGN KEY (category_id)
        REFERENCES categories (id)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id)
        REFERENCES user (id)
);

CREATE TABLE IF NOT EXISTS order_details (
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    order_id INT,
    product_id INT,
    beverage_id INT,
    baby_food_id INT,
    pet_id INT,
    snack_id INT,
    price DECIMAL(10 , 2 ) DEFAULT 0.0,
    FOREIGN KEY (order_id)
        REFERENCES orders (order_id),
    FOREIGN KEY (product_id)
        REFERENCES food_products (id),
    FOREIGN KEY (beverage_id)
        REFERENCES beverages (id),
    FOREIGN KEY (baby_food_id)
        REFERENCES baby_products (id),
    FOREIGN KEY (pet_id)
        REFERENCES pet_products (id),
    FOREIGN KEY (snack_id)
        REFERENCES snacks (id)
);

INSERT INTO market.categories (name, description)
VALUES 
("Харчі", "Харчі є невіддільною частиною щоденного раціону людини. Без них, неможливо жити!"),
("Напої", "Напої є тою частиною, що можна нехтувати. Проте, не забувайте про баланс води в організмі людини!"),
("Для дітей", "Діти є нашим продовженням та опорою в майбутньому, тож потурбуйтесь про їхнє здоров'я вже сьогодні!"),
("Корм для тварин", "Корм для тварин є необхідною складовою заботи про вашого домашнього улюбленця. Забезпечте йому смачне та збалансоване харчування для активного та щасливого життя!"),
("Закуски", "Закуски — це не лише втамування голоду між основними прийомами їжі, але й справжнє мистецтво насолоди смаком, яке додає різноманіття вашим кулінарним враженням.");

INSERT INTO market.food_products (name, category_id, price, image_url)
VALUES
("Картопля Сіфра", 1, 43.80, "https://fruit-time.ua/images/cache/products/c5/kartoplya-moloda-rozeva__462-500x500.jpeg"),
("Морква Натофі", 1, 10.00, "https://florium.ua/media/catalog/product/cache/1/file/9df78eab33525d08d6e5fb8d27136e95/m/o/morkov__natofi_2.jpg"),
("Насіння цибулі Люсі Semo 20 г", 1, 1841.40, "https://agriks.com.ua/images/detailed/20/semena-luka-lyusi-semo-20-g_1.jpg");

INSERT INTO market.beverages (name, category_id, price, image_url)
VALUES 
("Пиво Львівське 1715 светлое 4,5% 1,12л", 2, 56.30, "https://img3.zakaz.ua/upload.version_1.0.b3ecc5863abfa24a5bf4a3deefef8b81.1350x1350.jpeg"),
("Ром Bacardi Carta Negra 40% 0,7л", 2, 170.50, "https://novus.online/uploads/9/48736-7610113007952.jpg"),
("Віскі Wild Turkey Rye 40,5% 0,7л", 2, 129.99, "https://image.maudau.com.ua/size/origin/products/42/1f/9f/421f9ff1-489b-49e0-91c4-de1e2240b023.jpg");

INSERT INTO market.baby_products (name, category_id, price, image_url)
VALUES 
("Дитяче харчування \"Груша 100%\" органічне пюре (з 4 місяців) 125г", 3, 77.00, "https://i.goodwinehome.com.ua/16398-productMain/detskoe-pitanie-grusha-100-organicheskoe-pyure-s-4-mesyacev-125g--holle.jpg"),
("Дитяче харчування \"Яблуко і банан з абрикосом\" органічне пюре (з 6 місяців) 190г", 3, 99.00, "https://i.goodwinehome.com.ua/16403-productMain/detskoe-pitanie-yabloko-i-banan-s-abrikosom-organicheskoe-pyure-s-6-mesyacev-190g--holle.jpg"),
("Дитяче харчування \"Овочевий мікс\" органічне пюре (з 6 місяців) 190г", 3, 99.00, "https://i.goodwinehome.com.ua/16401-productMain/detskoe-pitanie-ovoshhnoj-miks-pyure-organicheskoe-s-6-mesyacev-190g--holle.jpg");

INSERT INTO market.pet_products (name, category_id, price, image_url)
VALUES 
("Kitekat (Кітікет) - Вологий корм з яловичиною в соусі для котів", 4, 39.00, "https://content.e-zoo.com.ua/files/Prods/prod_19304_16751286.jpg"),
("Сухий корм для собак Royal Canin X-Small Adult", 4, 867.00, "https://img.toba.ua/products/800/800/1021_sukhoy-korm-dlya-sobak-royal-canin-x-small-adult.jpg"),
("Корм для риб Природа Біовіт гранульований, 25 гр", 4, 34.00, "https://zooera.com.ua/image/cache/catalog/product/fish/korm-dlya-ryb-priroda-biovit-granulirovannyy-25-gr-6-800x800.jpg");

INSERT INTO market.snacks (name, category_id, price, image_url)
VALUES 
("Чіпси 110г Своя лінія картопляні зі смаком паприки", 5, 24.90, "https://src.zakaz.atbmarket.com/cache/photos/847/catalog_product_main_847.jpg"),
("Сухарі 240г Розумний вибір Гірчичне поле", 5, 19.70, "https://src.zakaz.atbmarket.com/cache/photos/2887/catalog_product_main_2887.jpg"),
("Крекери 400г Своя лінія солені", 5, 32.90, "https://src.zakaz.atbmarket.com/cache/photos/532/catalog_product_main_532.jpg");
