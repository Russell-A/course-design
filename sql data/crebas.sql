/*==============================================================*/
/* DBMS name:      Microsoft SQL Server 2008                    */
/* Created on:     2020/07/02 18:44:21                          */
/*==============================================================*/


if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('����') and o.name = 'FK_����_FK_�ɻ����_�ɻ��Ǽ�')
alter table ����
   drop constraint FK_����_FK_�ɻ����_�ɻ��Ǽ�
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('����') and o.name = 'FK_����_��������_����_����')
alter table ����
   drop constraint FK_����_��������_����_����
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('����') and o.name = 'FK_����_��������_����_����')
alter table ����
   drop constraint FK_����_��������_����_����
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('����') and o.name = 'FK_����_��������_��ͣ_����')
alter table ����
   drop constraint FK_����_��������_��ͣ_����
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('��Ʊ') and o.name = 'FK_��Ʊ_�û���_�û���')
alter table ��Ʊ
   drop constraint FK_��Ʊ_�û���_�û���
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('��Ʊ') and o.name = 'FK_��Ʊ_���̺�_���мƻ�����')
alter table ��Ʊ
   drop constraint FK_��Ʊ_���̺�_���мƻ�����
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('�ɻ��Ǽ�') and o.name = 'FK_�ɻ��Ǽ�_����_�ɻ���')
alter table �ɻ��Ǽ�
   drop constraint FK_�ɻ��Ǽ�_����_�ɻ���
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('���мƻ�����') and o.name = 'FK_���мƻ�����_������_����_����')
alter table ���мƻ�����
   drop constraint FK_���мƻ�����_������_����_����
go

if exists (select 1
            from  sysobjects
           where  id = object_id('����')
            and   type = 'U')
   drop table ����
go

if exists (select 1
            from  sysobjects
           where  id = object_id('�û���')
            and   type = 'U')
   drop table �û���
go

if exists (select 1
            from  sysobjects
           where  id = object_id('����')
            and   type = 'U')
   drop table ����
go

if exists (select 1
            from  sysobjects
           where  id = object_id('��Ʊ')
            and   type = 'U')
   drop table ��Ʊ
go

if exists (select 1
            from  sysobjects
           where  id = object_id('�ɻ��Ǽ�')
            and   type = 'U')
   drop table �ɻ��Ǽ�
go

if exists (select 1
            from  sysobjects
           where  id = object_id('�ɻ���')
            and   type = 'U')
   drop table �ɻ���
go

if exists (select 1
            from  sysobjects
           where  id = object_id('���мƻ�����')
            and   type = 'U')
   drop table ���мƻ�����
go

/*==============================================================*/
/* Table: ����                                                    */
/*==============================================================*/
create table ���� (
   ��������                 varchar(20)          not null,
   ������                  varchar(50)          not null,
   ���ڳ���                 varchar(20)          not null,
   constraint PK_���� primary key (��������)
)
go

/*==============================================================*/
/* Table: �û���                                                   */
/*==============================================================*/
create table �û��� (
   �û���                  varchar(20)          not null,
   �û�����                 varchar(20)          not null,
   �û�Ȩ��                 int                  not null,
   �û���ϵ��ʽ               varchar(20)          not null,
   constraint PK_�û��� primary key (�û���)
)
go

/*==============================================================*/
/* Table: ����                                                    */
/*==============================================================*/
create table ���� (
   ������                 varchar(10)          not null,
   ������������               varchar(20)          not null,
   ��ͣ��������               varchar(20)          null,
   �����������               varchar(20)          not null,
   �ɻ����                 varchar(10)          null,
   constraint PK_���� primary key (������),
   constraint AK_UQ_�ɻ����_���� unique (�ɻ����)
)
go

/*==============================================================*/
/* Table: ��Ʊ                                                    */
/*==============================================================*/
create table ��Ʊ (
   ��Ʊ���                 int                  identity,
   ���̺�                  int                  not null,
   ��������                 varchar(20)          not null,
   Ŀ�Ļ���                 varchar(20)          not null,
   ��λ���                 varchar(6)           not null,
   ��λ                   varchar(6)           not null,
   �û���                  varchar(20)          not null,
   �˿�����                 varchar(50)          not null,
   �˿��Ա�                 varchar(2)           not null
      constraint CKC_�˿��Ա�_��Ʊ check (�˿��Ա� in ('��','Ů')),
   �˿����                 varchar(10)          not null
      constraint CKC_�˿����_��Ʊ check (�˿���� in ('����','С��','�и�','����','�м�','����','<Val8>')),
   "�˿����֤��/���պ�"         varchar(20)          not null,
   �˿���ϵ��ʽ               varchar(20)          not null,
   constraint PK_��Ʊ primary key (��Ʊ���)
)
go

/*==============================================================*/
/* Table: �ɻ��Ǽ�                                                  */
/*==============================================================*/
create table �ɻ��Ǽ� (
   �ɻ����                 varchar(10)          not null,
   ����                   varchar(50)          not null,
   ע������                 smalldatetime        not null,
   ʹ������                 tinyint              not null,
   ������Ϣ                 text                 null,
   constraint PK_�ɻ��Ǽ� primary key (�ɻ����)
)
go

/*==============================================================*/
/* Table: �ɻ���                                                   */
/*==============================================================*/
create table �ɻ��� (
   ����                   varchar(50)          not null,
   ���������                smallint             null,
   ͷ�Ȳ�����                smallint             null,
   ���ò�����                smallint             null,
   ������                  real                 not null,
   ������                 real                 not null,
   constraint PK_�ɻ��� primary key (����)
)
go

/*==============================================================*/
/* Table: ���мƻ�����                                                */
/*==============================================================*/
create table ���мƻ����� (
   ���̺�                  int                  identity,
   ������                 varchar(10)          not null,
   �ƻ�����ʱ��               datetime             not null,
   �ƻ����ﾭͣ����ʱ��           datetime             null,
   �ƻ��Ӿ�ͣ��������ʱ��          datetime             null,
   �ƻ�����ʱ��               datetime             not null,
   "���òգ���ʼ-���ʣ����λ"     smallint             null,
   "����գ���ʼ-���ʣ����λ"     smallint             null,
   "ͷ�Ȳգ���ʼ-���ʣ����λ"     smallint             null,
   "���òգ���ͣ-���ʣ����λ"     smallint             null,
   "����գ���ͣ-���ʣ����λ"     smallint             null,
   "ͷ�Ȳգ���ͣ-���ʣ����λ"     smallint             null,
   "���òգ���ʼ-��ͣ��ʣ����λ"     smallint             null,
   "����գ���ʼ-��ͣ��ʣ����λ"     smallint             null,
   "ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ"     smallint             null,
   "Ʊ�ۣ���ʼ-������òգ�"      money                null,
   "Ʊ�ۣ���ʼ-��ͣ�����òգ�"      money                null,
   "Ʊ�ۣ���ͣ-������òգ�"      money                null,
   "Ʊ�ۣ���ʼ-�������գ�"      money                null,
   "Ʊ�ۣ���ʼ-��ͣ������գ�"      money                null,
   "Ʊ�ۣ���ͣ-�������գ�"      money                null,
   "Ʊ�ۣ���ʼ-���ͷ�Ȳգ�"      money                null,
   "Ʊ�ۣ���ʼ-��ͣ��ͷ�Ȳգ�"      money                null,
   "Ʊ�ۣ���ͣ-���ͷ�Ȳգ�"      money                null,
   constraint PK_���мƻ����� primary key (���̺�)
)
go

alter table ����
   add constraint FK_����_FK_�ɻ����_�ɻ��Ǽ� foreign key (�ɻ����)
      references �ɻ��Ǽ� (�ɻ����)
go

alter table ����
   add constraint FK_����_��������_����_���� foreign key (������������)
      references ���� (��������)
go

alter table ����
   add constraint FK_����_��������_����_���� foreign key (�����������)
      references ���� (��������)
go

alter table ����
   add constraint FK_����_��������_��ͣ_���� foreign key (��ͣ��������)
      references ���� (��������)
go

alter table ��Ʊ
   add constraint FK_��Ʊ_�û���_�û��� foreign key (�û���)
      references �û��� (�û���)
go

alter table ��Ʊ
   add constraint FK_��Ʊ_���̺�_���мƻ����� foreign key (���̺�)
      references ���мƻ����� (���̺�)
go

alter table �ɻ��Ǽ�
   add constraint FK_�ɻ��Ǽ�_����_�ɻ��� foreign key (����)
      references �ɻ��� (����)
go

alter table ���мƻ�����
   add constraint FK_���мƻ�����_������_����_���� foreign key (������)
      references ���� (������)
go

