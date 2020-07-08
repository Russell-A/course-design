USE air
GO
CREATE TRIGGER tr_flight
ON ���мƻ����� AFTER INSERT
AS
DECLARE @flight_no varchar(50), @flight_type varchar(50), @plane_num varchar(50), @fly_no int
DECLARE @first_num int, @business_num int, @economy_num int
set @fly_no = (SELECT ���̺� from inserted)
set @flight_no = (SELECT ������ from inserted)
set @plane_num = (SELECT �ɻ���� FROM ���� WHERE ������ = @flight_no)
set @flight_type = (SELECT ���� FROM �ɻ��Ǽ� where �ɻ���� = @plane_num )
set @first_num = (SELECT ͷ�Ȳ����� FROM �ɻ��� WHERE ���� = @flight_type)
set @business_num = (SELECT ��������� FROM �ɻ��� WHERE ���� = @flight_type)
set @economy_num = (SELECT ���ò����� FROM �ɻ��� WHERE ���� = @flight_type)
IF @economy_num = 0
SET @economy_num = null
IF @business_num = 0
SET @business_num = null
IF @first_num = 0
SET @first_num = null
update ���мƻ�����
set [����գ���ʼ-���ʣ����λ] = @business_num, [����գ���ʼ-��ͣ��ʣ����λ] =@business_num, [����գ���ͣ-���ʣ����λ] = @business_num,
[���òգ���ʼ-���ʣ����λ] = @economy_num, [���òգ���ʼ-��ͣ��ʣ����λ]  = @economy_num, [���òգ���ͣ-���ʣ����λ]  = @economy_num,
[ͷ�Ȳգ���ʼ-���ʣ����λ]  = @first_num,[ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ]   = @first_num,[ͷ�Ȳգ���ͣ-���ʣ����λ]   = @first_num
where ���̺� = @fly_no
GO

--ԭ�����������⡭������
DROP trigger tr_refund_ticket
GO
--����һ�� 
CREATE trigger tr_refund_ticket 
ON ��Ʊ AFTER DELETE
AS 
DECLARE @seatnum int, @seat varchar(20), @flight1 varchar(20) ,@flight2 varchar(20),@begin varchar(20), @terminal varchar(20) --flight1 ���̺� flight2 ����� /������������� 
SELECT @flight1 = ���̺�,@seat = ��λ, @begin = ��������, @terminal = Ŀ�Ļ���  , @seatnum = ��λ��� FROM deleted
SELECT @flight2 = ������ FROM ���мƻ����� WHERE ���̺� = @flight1 

IF exists (select * from ������ͣ where ������ = @begin and Ŀ�ĵ� = @terminal and ������ = @flight2)
BEGIN
	IF @seat = '�����'
	BEGIN
		Update ���мƻ����� 
			set [����գ���ʼ-��ͣ��ʣ����λ] = [����գ���ʼ-��ͣ��ʣ����λ] + 1  where ���̺� = @flight1
		IF @seatnum NOT IN (SELECT ��λ��� FROM ��Ʊ WHERE ���̺� = @flight1 AND ��λ = @seat)
			UPDATE ���мƻ�����
				SET [����գ���ʼ-���ʣ����λ] = [����գ���ʼ-���ʣ����λ] + 1  where ���̺� = @flight1 
	END
	ELSE IF @seat = 'ͷ�Ȳ�'
	BEGIN
		Update ���мƻ����� 
			SET [ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ] = [ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ] + 1  where ���̺� = @flight1
		IF @seatnum NOT IN (SELECT ��λ��� FROM ��Ʊ WHERE ���̺� = @flight1 AND ��λ = @seat)
			Update ���мƻ�����
				set [ͷ�Ȳգ���ʼ-���ʣ����λ] = [ͷ�Ȳգ���ʼ-���ʣ����λ] + 1  where ���̺� = @flight1 
	END
	ELSE
	BEGIN
		Update ���мƻ����� 
			set [���òգ���ʼ-��ͣ��ʣ����λ] = [���òգ���ʼ-��ͣ��ʣ����λ] + 1  where ���̺� = @flight1
		IF @seatnum NOT IN (SELECT ��λ��� FROM ��Ʊ WHERE ���̺� = @flight1 AND ��λ = @seat)
			Update ���мƻ�����
				set [���òգ���ʼ-���ʣ����λ] = [���òգ���ʼ-���ʣ����λ] + 1  where ���̺� = @flight1 
	END
END
IF exists (select * from ��ͣ���� where ������ = @begin and Ŀ�ĵ� = @terminal and ������ = @flight2)
BEGIN
		IF @seat = '�����'
	BEGIN
		Update ���мƻ����� 
			set [����գ���ͣ-���ʣ����λ] = [����գ���ͣ-���ʣ����λ] + 1  where ���̺� = @flight1
		IF @seatnum NOT IN (SELECT ��λ��� FROM ��Ʊ WHERE ���̺� = @flight1 AND ��λ = @seat)
			Update ���мƻ�����
				set [����գ���ʼ-���ʣ����λ] = [����գ���ʼ-���ʣ����λ] + 1  where ���̺� = @flight1 
	END
	ELSE IF @seat = 'ͷ�Ȳ�'
	BEGIN
		Update ���мƻ����� 
			set [ͷ�Ȳգ���ͣ-���ʣ����λ] = [ͷ�Ȳգ���ͣ-���ʣ����λ] + 1  where ���̺� = @flight1
		IF @seatnum NOT IN (SELECT ��λ��� FROM ��Ʊ WHERE ���̺� = @flight1 AND ��λ = @seat)
			Update ���мƻ�����
				set [ͷ�Ȳգ���ʼ-���ʣ����λ] = [ͷ�Ȳգ���ʼ-���ʣ����λ] + 1  where ���̺� = @flight1 
	END
	ELSE
	BEGIN
		Update ���мƻ����� 
			set [���òգ���ͣ-���ʣ����λ] = [���òգ���ͣ-���ʣ����λ] + 1  where ���̺� = @flight1
		IF @seatnum NOT IN (SELECT ��λ��� FROM ��Ʊ WHERE ���̺� = @flight1 AND ��λ = @seat)
			Update ���мƻ�����
				set [���òգ���ʼ-���ʣ����λ] = [���òգ���ʼ-���ʣ����λ] + 1  where ���̺� = @flight1 
	END
END
IF exists (select * from �������� where ������ = @begin and Ŀ�ĵ� = @terminal and ������ = @flight2)
BEGIN
	IF @seat = '�����'
	begin
		Update ���мƻ����� 
			set [����գ���ʼ-���ʣ����λ] = [����գ���ʼ-���ʣ����λ] + 1  where ���̺� = @flight1 
		UPdate ���мƻ�����
			set [����գ���ʼ-��ͣ��ʣ����λ] = [����գ���ʼ-��ͣ��ʣ����λ] + 1  where ���̺� = @flight1 and [����գ���ʼ-��ͣ��ʣ����λ] is not NULL
		Update ���мƻ�����
			set [����գ���ͣ-���ʣ����λ] = [����գ���ͣ-���ʣ����λ] + 1  where ���̺� = @flight1 and [����գ���ͣ-���ʣ����λ] is not NULL	
	end
	IF @seat = 'ͷ�Ȳ�'
	BEGIN
		Update ���мƻ����� 
			set [ͷ�Ȳգ���ʼ-���ʣ����λ] = [ͷ�Ȳգ���ʼ-���ʣ����λ] + 1  where ���̺� = @flight1 
		Update ���мƻ�����
			set [ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ] = [ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ] + 1  where ���̺� = @flight1 and [ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ] is not NULL
		Update ���мƻ�����
			set [ͷ�Ȳգ���ͣ-���ʣ����λ] = [ͷ�Ȳգ���ͣ-���ʣ����λ] + 1  where ���̺� = @flight1 and [ͷ�Ȳգ���ͣ-���ʣ����λ] is not NULL
	END
	IF @seat = '���ò�'
	BEGIN
	Update ���мƻ����� 
			set [���òգ���ʼ-���ʣ����λ] = [���òգ���ʼ-���ʣ����λ] + 1  where ���̺� = @flight1
	Update ���мƻ�����
			set [���òգ���ʼ-��ͣ��ʣ����λ] = [���òգ���ʼ-��ͣ��ʣ����λ] + 1  where ���̺� = @flight1 and [���òգ���ʼ-��ͣ��ʣ����λ] is not NULL
	Update ���мƻ�����
			set [���òգ���ͣ-���ʣ����λ] = [���òգ���ͣ-���ʣ����λ] + 1  where ���̺� = @flight1 and [���òգ���ͣ-���ʣ����λ] is not NULL
	END
END


