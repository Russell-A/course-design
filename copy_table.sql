USE air
GO

CREATE PROC copy_table  @flight_no int
AS
SELECT * INTO ��˽��ѯ FROM ��Ʊ WHERE ���̺� = @flight_no
ALTER TABLE ��˽��ѯ ADD mid int
EXEC('UPDATE ��˽��ѯ SET mid = ��Ʊ���')
ALTER TABLE ��˽��ѯ DROP COLUMN ��Ʊ���
exec sp_rename '��˽��ѯ.mid','��Ʊ���'
ALTER TABLE ��˽��ѯ ADD ��� int IDENTITY(1,1)
