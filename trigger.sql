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

CREATE trigger tr_refund_ticket 
ON ��Ʊ AFTER DELETE
AS 
Declare @seat varchar(20), @flight1 varchar(20) ,@flight2 varchar(20),@begin varchar(20), @terminal varchar(20) --flight1 ���̺� flight2 ����� /������������� 
select @flight1 = ���̺�,@seat = ��λ, @begin = ��������, @terminal = Ŀ�Ļ���  from deleted
select @flight2 = ������ from ���мƻ����� where ���̺� = @flight1 

IF exists (select * from ������ͣ where ������ = @begin and Ŀ�ĵ� = @terminal and ������ = @flight2)
BEGIN
	IF @seat = '�����'
		Update ���мƻ����� 
			set [����գ���ʼ-��ͣ��ʣ����λ] = [����գ���ʼ-��ͣ��ʣ����λ] + 1  where ���̺� = @flight1
	ELSE IF @seat = 'ͷ�Ȳ�'
		Update ���мƻ����� 
			set [ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ] = [ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ] + 1  where ���̺� = @flight1
	ELSE 
	Update ���мƻ����� 
			set [���òգ���ʼ-��ͣ��ʣ����λ] = [���òգ���ʼ-��ͣ��ʣ����λ] + 1  where ���̺� = @flight1
END
IF exists (select * from ��ͣ���� where ������ = @begin and Ŀ�ĵ� = @terminal and ������ = @flight2)
BEGIN
	IF @seat = '�����'
		Update ���мƻ����� 
			set [����գ���ͣ-���ʣ����λ] = [����գ���ͣ-���ʣ����λ] + 1  where ���̺� = @flight1
	ELSE IF @seat = 'ͷ�Ȳ�'
		Update ���мƻ����� 
			set [ͷ�Ȳգ���ͣ-���ʣ����λ] = [ͷ�Ȳգ���ͣ-���ʣ����λ] + 1  where ���̺� = @flight1
	ELSE 
	Update ���мƻ����� 
			set [���òգ���ͣ-���ʣ����λ] = [���òգ���ͣ-���ʣ����λ] + 1  where ���̺� = @flight1
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


