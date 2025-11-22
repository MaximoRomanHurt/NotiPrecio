
-- PostgreSQL schema for productos de primera necesidad

CREATE TABLE IF NOT EXISTS producto (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    categoria VARCHAR(255),
    unidad VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS precio_historico (
    id_precio SERIAL PRIMARY KEY,
    id_producto INTEGER REFERENCES producto(id_producto) ON DELETE CASCADE,
    tipo_precio VARCHAR(100),
    precio DOUBLE PRECISION,
    fecha_registro DATE
);

CREATE TABLE IF NOT EXISTS diferencia_precio (
    id_diferencia SERIAL PRIMARY KEY,
    id_producto INTEGER REFERENCES producto(id_producto) ON DELETE CASCADE,
    id_precio_fijo INTEGER REFERENCES precio_historico(id_precio),
    id_precio_var INTEGER REFERENCES precio_historico(id_precio),
    diferencia DOUBLE PRECISION,
    creada_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS noticia (
    id_noticia SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    contenido TEXT,
    fuente TEXT,
    fecha_publicacion TEXT
);

CREATE TABLE IF NOT EXISTS producto_noticia (
    id_producto INTEGER REFERENCES producto(id_producto) ON DELETE CASCADE,
    id_noticia INTEGER REFERENCES noticia(id_noticia) ON DELETE CASCADE,
    PRIMARY KEY (id_producto, id_noticia)
);

CREATE TABLE IF NOT EXISTS notificacion (
    id_notificacion SERIAL PRIMARY KEY,
    id_diferencia INTEGER REFERENCES diferencia_precio(id_diferencia),
    id_producto INTEGER REFERENCES producto(id_producto),
    mensaje TEXT,
    tipo VARCHAR(50),
    canal VARCHAR(50),
    activa BOOLEAN DEFAULT TRUE,
    enviada BOOLEAN DEFAULT FALSE,
    programada_para TIMESTAMP,
    creada_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
