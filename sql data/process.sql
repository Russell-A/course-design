use air
create table ������ (
���̺� int not null,
���� int default 0,
foreign key(���̺�) references ���мƻ�����(���̺�) on delete cascade on update cascade
)
go
insert into ������(���̺�) select ���̺� from ���мƻ�����
go