CREATE TABLE usuario (
	cod SERIAL PRIMARY KEY,
	nome VARCHAR(150) NOT NULL,
	cpf VARCHAR(14) UNIQUE NOT NULL,
	email VARCHAR(50) UNIQUE NOT NULL,
	senha VARCHAR(16) NOT NULL,
	telefone VARCHAR(16),
	tipo_usuario VARCHAR(16) NOT NULL
);

CREATE TABLE nota (
	cod SERIAL PRIMARY KEY,
	valor FLOAT,
	aluno_cod INTEGER,
	professor_cod INTEGER,
	disciplina VARCHAR(50),
	bimestre INTEGER,
	FOREIGN KEY(aluno_cod) REFERENCES usuario(cod),
	FOREIGN KEY(professor_cod) REFERENCES usuario(cod)
);


INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Admnistrador', '000.000.000-00', 'admin@gmail.com', 'admin', '0000000000', 'ADMIN');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Nícolas Jessé Amaral Marques', '439.053.520-01', 'nicolasnekar@gmail.com', 'coxinha123', '8391612065', 'ALUNO');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Adriel Higor', '547.329.410-36', 'adrielhacker@gmail.com', 'coxinha123', '8398120657', 'ALUNO');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('William', '295.229.420-81', 'falouwilliam@gmail.com', 'coxinha123', '8391155110', 'ALUNO');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Sharlinskya Klismenia', '984.170.220-74', 'klisgata@gmail.com', 'coxinha123', '8396493515', 'ALUNO');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Jeysianne', '694.729.720-63', 'jeysachora@gmail.com', 'coxinha123', '8382008745', 'ALUNO');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Guilherme', '956.327.050-99', 'modelocontato@gmail.com', 'coxinha123', '8393776868', 'ALUNO');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Katiusc', '551.282.310-89', 'top@gmail.com', 'coxinha123', '8391234568', 'ALUNO');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Maria José', '170.219.770-00', 'kkkkkk@gmail.com', 'coxinha123', '8312345678', 'PROFESSOR');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Valéria', '531.737.260-73', 'perxpectiva@gmail.com', 'coxinha123', '8398745869', 'PROFESSOR');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Núbia', '629.307.780-67', 'quebreiaperna@gmail.com', 'coxinha123', '8365257894', 'PROFESSOR');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Welinsson', '589.683.970-74', 'jjjjjjkkkk@gmail.com', 'coxinha123', '8325143658', 'PROFESSOR');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Virginia', '395.003.710-14', 'predicado@gmail.com', 'coxinha123', '8392516352', 'PROFESSOR');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Gustavo', '911.748.030-29', 'queroum10@gmail.com', 'coxinha123', '8325144785', 'PROFESSOR');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('George', '416.020.870-32', 'fera@gmail.com', 'coxinha123', '8345567898', 'PROFESSOR');
INSERT INTO usuario (nome, cpf, email, senha, telefone, tipo_usuario) VALUES('Saymon', '326.332.010-67', 'rapadura@gmail.com', 'coxinha123', '8302526332', 'PROFESSOR');

INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 9, 'SOCIOLOGIA', 1);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 9, 'SOCIOLOGIA', 2);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 9, 'SOCIOLOGIA', 3);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 9, 'SOCIOLOGIA', 4);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 10, 'HISTORIA', 1);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 10, 'HISTORIA', 2);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 10, 'HISTORIA', 3);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 10, 'HISTORIA', 4);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(4, 2, 11, 'EDUCAÇAO FISICA', 1);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(4, 2, 11, 'EDUCAÇAO FISICA', 2);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(4, 2, 11, 'EDUCAÇAO FISICA', 3);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(4, 2, 11, 'EDUCAÇAO FISICA', 4);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(7, 2, 12, 'MATEMATICA', 1);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(7, 2, 12, 'MATEMATICA', 2);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(7, 2, 12, 'MATEMATICA', 3);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(7, 2, 12, 'MATEMATICA', 4);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(8, 2, 13, 'PORTUGUES', 1);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(8, 2, 13, 'PORTUGUES', 2);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(8, 2, 13, 'PORTUGUES', 3);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(8, 2, 13, 'PORTUGUES', 4);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 14, 'ESTRUTURA', 1);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 14, 'ESTRUTURA', 2);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 14, 'ESTRUTURA', 3);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 14, 'ESTRUTURA', 4);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 15, 'SO', 1);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 15, 'SO', 2);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 15, 'SO', 3);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(10, 2, 15, 'SO', 4);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(8, 2, 16, 'REDES', 1);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(8, 2, 16, 'REDES', 2);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(8, 2, 16, 'REDES', 3);
INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES(8, 2, 16, 'REDES', 4);