CREATE TABLE cursos(
   id_cursos INTEGER PRIMARY KEY, -- integer-int
   nome_dos_cursos TEXT NOT NULL,
   duracao TEXT NOT NULL,
   preco FLOAT,
   categoria TEXT NOT NULL
);

-- Inserindo alguns valores
INSERT INTO cursos VALUES (1, 'Informática', '120h', 1200.00, 'Tecnologia');
INSERT INTO cursos VALUES (2, 'Inglês', '220h', 2200.00, 'Idiomas');
INSERT INTO cursos VALUES (3, 'Matemática', '100h', 1500.00, 'Exatas');
INSERT INTO cursos VALUES (4, 'História', '80h', 1000.00, 'Humanas');
INSERT INTO cursos VALUES (5, 'Química', '90h', 1300.00, 'Exatas');
INSERT INTO cursos VALUES (6, 'Física', '110h', 1400.00, 'Exatas');
INSERT INTO cursos VALUES (7, 'Biologia', '95h', 1250.00, 'Ciências');
INSERT INTO cursos VALUES (8, 'Geografia', '85h', 1100.00, 'Humanas');
INSERT INTO cursos VALUES (9, 'Programação', '150h', 2000.00, 'Tecnologia');
INSERT INTO cursos VALUES (10, 'Francês', '200h', 2100.00, 'Idiomas');

SELECT * FROM cursos;



CREATE TABLE contatos (
   id_telefone VARCHAR(20) PRIMARY KEY, -- usando VARCHAR com comprimento especificado
   email TEXT NOT NULL,
   filial TEXT NOT NULL,
   instagram TEXT NOT NULL,
   linkedin TEXT NOT NULL
);


-- Inserindo alguns valores
INSERT INTO contatos VALUES ('0000-0000', 'curso@exemplo.com', 'Catete', '@curso_catete', 'linkedin.com/curso-catete');
INSERT INTO contatos VALUES ('1111-1111', 'curso@exemplo.com', 'Copacabana', '@curso_copacabana', 'linkedin.com/curso-copacabana');
INSERT INTO contatos VALUES ('2222-2222', 'curso@exemplo.com', 'Botafogo', '@curso_botafogo', 'linkedin.com/curso-botafogo');
INSERT INTO contatos VALUES ('3333-3333', 'curso@exemplo.com', 'Ipanema', '@curso_ipanema', 'linkedin.com/curso-ipanema');
INSERT INTO contatos VALUES ('4444-4444', 'curso@exemplo.com', 'Leblon', '@curso_leblon', 'linkedin.com/curso-leblon');
INSERT INTO contatos VALUES ('5555-5555', 'curso@exemplo.com', 'Tijuca', '@curso_tijuca', 'linkedin.com/curso-tijuca');
INSERT INTO contatos VALUES ('6666-6666', 'curso@exemplo.com', 'Barra da Tijuca', '@curso_barra', 'linkedin.com/curso-barra');
INSERT INTO contatos VALUES ('7777-7777', 'curso@exemplo.com', 'Recreio', '@curso_recreio', 'linkedin.com/curso-recreio');
INSERT INTO contatos VALUES ('8888-8888', 'curso@exemplo.com', 'Centro', '@curso_centro', 'linkedin.com/curso-centro');

-- Consultando as inserções realizadas
SELECT * FROM contatos;
