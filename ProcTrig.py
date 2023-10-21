CREATE OR REPLACE FUNCTION update_application_mincount()
RETURNS TRIGGER AS $$
DECLARE
    total_mincount INTEGER;
BEGIN
    -- Складываем все значения MinCount из Req относящиеся к одной Category
    SELECT SUM(MinCount) INTO total_mincount FROM Req WHERE Category = NEW.Cath;

    -- Обновляем значение MinCount в записи Application
    UPDATE Application SET MinCount = total_mincount WHERE idA = NEW.idA;

    RETURN NEW;
END;

CREATE TRIGGER application_mincount_trigger
AFTER INSERT ON Application
FOR EACH ROW
EXECUTE FUNCTION update_application_mincount();


-- Триггер для таблицы Application
CREATE OR REPLACE FUNCTION generate_idA()
RETURNS TRIGGER AS $$
BEGIN
    -- Генерация значения idA
    NEW.idA := NEXTVAL('application_idA_seq');
    RETURN NEW;
END;


CREATE TRIGGER generate_idA_trigger
BEFORE INSERT ON Application
FOR EACH ROW
EXECUTE FUNCTION generate_idA();

-- Триггер для таблицы ApplEl
CREATE OR REPLACE FUNCTION create_applEl()
RETURNS TRIGGER AS $$
BEGIN
    -- Генерация значения idAe
    NEW.idAe := NEW.idA;

    -- Создание записи в таблице ApplEl
    INSERT INTO ApplEl (idAe, idAp)
    VALUES (NEW.idAe, NEW.idA);

    RETURN NEW;
END;




CREATE TRIGGER add_pr_trigger
AFTER INSERT ON Application
FOR EACH ROW
EXECUTE FUNCTION add_pr();


CREATE PROCEDURE GetPhotopathByPR(IN PR_Value INT)
BEGIN
    SELECT ph.Photopath
    FROM ApplEl ae
    JOIN PhReq pr ON ae.PR = pr.id
    JOIN Photo ph ON pr.idPho = ph.idPh
    WHERE ae.PR = PR_Value;
END



CALL GetPhotopathByPR(твое_значение_PR);
