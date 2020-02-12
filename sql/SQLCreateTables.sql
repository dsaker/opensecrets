--Campaign Finance Data

CREATE TABLE Candidates( 
 	Cycle char(4) NOT NULL, 
 	FECCandID char(9) NOT NULL, 
 	CID char(9) PRIMARY KEY, 
 	FirstLastP varchar(50) NULL, 
 	Party char(1) NULL, 
 	DistIDRunFor char(4) NULL, 
 	DistIDCurr char(4) NULL, 
 	CurrCand char(1) NULL, 
 	CycleCand char(1) NULL, 
 	CRPICO char(1) NULL, 
 	RecipCode char(2) NULL, 
 	NoPacs char(1) NULL 
);
 
 
CREATE TABLE FECCommittees ( 
 	Cycle char(4) NOT NULL, 
 	CmteID char(9) PRIMARY KEY, 
 	PACShort varchar(50) NULL, 
 	Affiliate varchar(50) NULL, 
 	UltOrg varchar(50) NULL, 
 	RecipID char(9) NULL, 
 	RecipCode char(2) NULL, 
 	FECCandID char(9) NULL, 
 	Party char(1) NULL, 
 	PrimCode char(5) NULL, 
 	Source char(10) NULL, 
	Sensitive char(1) NULL, 
 	Foreign bit NOT NULL, 
 	Active int NULL 
);
 
CREATE TABLE PACtoCandidates ( 
 	Cycle char(4) NOT NULL, 
 	FECRecNo char(19)  NOT NULL, 
    PACID char(9)  NOT NULL, 
 	CID char(9)  NULL, 
 	Amount int DEFAULT (0), 
 	Date smalldatetime NULL, 
 	RealCode char(5)  NULL, 
 	Type char(3)  NULL, 
 	DI char(1)  NOT NULL, 
 	FECCandID char(9)  NULL,
	PRIMARY KEY (CID, PACID) 
);
 
CREATE TABLE PACtoPAC ( 
 	Cycle char(4) NOT NULL, 
 	FECRecNo char(19)  NOT NULL, 
 	FilerID char(9)  NOT NULL, 
 	DonorCmte varchar(50)  NULL, 
 	ContribLendTrans varchar(50)  NULL, 
 	City varchar(30)  NULL, 
 	State char(2)  NULL, 
 	Zip char(5)  NULL, 
 	FECOccEmp varchar(38)  NULL, 
 	PrimCode char(5)  NULL, 
 	Date smalldatetime NULL, 
 	Amount float NULL, 
 	RecipID char(9)  NULL, 
 	Party char(1)  NULL, 
 	OtherID char(9)  PRIMARY KEY, 
 	RecipCode char(2)  NULL, 
 	RecipPrimcode char(5)  NULL, 
 	Amend char(1)  NULL, 
 	Report char(3)  NULL, 
 	PG char(1)  NULL, 
 	Microfilm char(11)  NULL, 
 	Type char(3)  NULL, 
 	Realcode char(5)  NULL, 
 	Source char(5)  NULL,
	PRIMARY KEY (Cycle, FECRecNo) 
);

CREATE TABLE Individual( 
 	Cycle char(4) NOT NULL, 
 	FECTransID char(19) NOT NULL, 
 	ContribID char(12) NULL, 
    Contrib varchar(50) NULL, 
    RecipID char(9) NULL, 
 	Orgname varchar(50) NULL, 
 	UltOrg varchar(50) NULL, 
 	RealCode char(5) NULL, 
 	Date datetime NULL, 
 	Amount int NULL, 
 	City varchar (30) NULL, 
 	State char (2) NULL, 
    Zip char (5) NULL, 
 	Recipcode char (2) NULL, 
 	Type char(3) NULL, 
 	CmteID char(9) NULL, 
 	OtherID char(9) NULL, 
 	Gender char(1) NULL, 
    Microfilm varchar(11) NULL, 
 	Occupation varchar(38) NULL, 
    Employer varchar(38) NULL,
    Source char(5) NULL,
	PRIMARY KEY (Cycle, FECTransID)  
);

CREATE TABLE Expenditures( 
 	Cycle char(4) NOT NULL, 
 	TransID char(20) , 
 	CRPFilerid char(9) , 
 	recipcode char(2) , 
 	pacshort varchar(50) , 
 	CRPRecipName varchar(90) , 
 	ExpCode char(3) , 
 	Amount decimal(12, 0) NOT NULL, 
 	Date date NULL, 
 	City varchar(30) , 
 	State char(2) , 
 	Zip char(9) , 
 	CmteID_EF char(9) , 
 	CandID char(9) , 
 	Type char(3) , 
 	Descrip varchar(100) , 
 	PG char(5) , 
 	ElecOther varchar(20) , 
 	EntType char(3) , 
 	Source char(5) ) ,
	PRIMARY KEY (Cycle, TransID)
);

--Lobbying

CREATE TABLE dbo.lobbying( 
 	uniqid varchar(36) NOT NULL, 
 	registrant_raw varchar(110) NULL, 
 	registrant varchar(50) NULL, 
 	isfirm char(1) NULL, 
 	client_raw varchar(110) NULL, 
 	client varchar(50) NULL, 
 	ultorg varchar(50) NULL, 
 	amount float NULL, 
 	catcode char(5) NULL, 
 	source char (5) NULL, 
 	self char(1) NULL, 
 	IncludeNSFS char(1) NULL, 
 	use char(1) NULL, 
 	ind char(1) NULL, 
 	year char(4) NULL, 
 	type char(4) NULL, 
 	typelong varchar(50) NULL, 
 	affiliate char(1) NULL, 
) ON PRIMARY 
 
CREATE TABLE dbo.Lobbyists( 
 	uniqID varchar(36) NOT NULL, 
 	lobbyist varchar(50) NULL, 
 	lobbyist_raw varchar(50) NULL, 
 	lobbyist_id char(12) NULL, 
 	year char(4) NULL, 
 	Official Position varchar(100) NULL, 
 	cid char (9) NULL, 
 	formercongmem char(1) NULL 
) ON PRIMARY 

CREATE TABLE dbo.LobbyIndus( 
 	client varchar(50) NULL, 
 	sub varchar(50) NULL, 
 	total float NULL, 
 	year char(4) NULL, 
 	catcode char(5) NULL 
) ON PRIMARY 
 
 
CREATE TABLE dbo.lobbyagency( 
 	uniqID varchar(36) NOT NULL, 
 	agencyID char(3) NOT NULL, 
 	Agency varchar(80) NULL 
) ON PRIMARY 

CREATE TABLE dbo.lobbyissue( 
 	SI_ID int NOT NULL, 
 	uniqID varchar(36) NOT NULL, 
 	issueID char(3) NOT NULL, 
 	issue varchar(50) NULL, 
 	SpecificIssue varchar(max) NULL, 
 	year char (4) NULL 
) ON PRIMARY 
 
 
CREATE TABLE dbo.lob_bills( 
 	B_ID int NULL, 
 	si_id int NULL, 
 	CongNo char(3) NULL, 
    Bill_Name varchar(15) NOT NULL 
) ON PRIMARY  
 
CREATE TABLE dbo.lob_rpt( 
 	TypeLong varchar (50) NOT NULL, 
 	Typecode char(4) NOT NULL 
) ON PRIMARY 

--Personal Finances

CREATE TABLE dbo.Agreement( 
 	ID varchar(15)  NOT NULL, 
 	Chamber char(1)  NULL, 
 	CID char(9)  NULL, 
 	CalendarYear char(2)  NOT NULL, 
 	ReportType char(1)  NULL, 
 	AgreementDate1 smalldatetime NULL, 
 	AgreementDate1Text char(50)  NULL, 
 	AgreementDate2 smalldatetime NULL, 
 	AgreementDate2Text char(50)  NULL, 
 	AgreementParty1 varchar(100)  NULL, 
 	Orgname varchar(40)  NULL, 
 	Ultorg varchar(40)  NULL, 
 	Realcode char(5)  NULL, 
 	Source char(5)  NULL, 
 	AgreementParty1Loc varchar(50)  NULL, 
 	AgreementParty2 varchar(100)  NULL, 
 	Orgname2 varchar(40)  NULL, 
 	Ultorg2 varchar(40)  NULL, 
 	Realcode2 char(5)  NULL, 
 	Source2 char(5)  NULL, 
 	AgreementTerms varchar(1500)  NULL, 
 	Dupe char(1)  NULL 
) ON PRIMARY 

CREATE TABLE dbo.PFD_Asset( 
 	ID varchar(15) NOT NULL, 
 	Chamber char(1) NULL, 
 	CID char(9) NULL, 
 	CalendarYear char(2) NOT NULL, 
 	ReportType char(1) NULL, 
 	SenAB char(1) NULL, 
 	AssetSpouseJointDep char(1) NULL, 
 	AssetSource varchar(100) NULL, 
 	Orgname varchar(40) NULL, 
 	Ultorg varchar(40) NULL, 
 	Realcode char(5) NULL, 
 	Source char(5) NULL, 
    AssetDescrip varchar(100) NULL, 
    Orgname2 varchar(40) NULL, 
    Ultorg2 varchar(40) NULL, 
    Realcode2 char(5) NULL, 
    Source2 char(5) NULL, 
    AssetSourceLocation varchar(50) NULL, 
    AssetValue char(2) NULL, 
    AssetExactValue decimal(18, 0) NULL, 
    AssetDividends char(1) NULL, 
    AssetRent char(1) NULL, 
    AssetInterest char(1) NULL, 
    AssetCapitalGains char(1) NULL,  	
    AssetExemptedFund char(1) NULL, 
 	AssetExemptedTrust char(1) NULL, 
 	AssetQualifiedBlindTrust char(1) NULL, 
 	AssetTypeCRP char(2) NULL, 
 	OtherTypeIncome varchar(100) NULL, 
 	AssetIncomeAmtRange varchar(4) NULL, 
 	AssetIncomeAmountText varchar(10) NULL, 
 	AssetIncomeAmt money NULL, 
 	AssetPurchased char(1) NULL, 
 	AssetSold char(1) NULL, 
 	AssetExchanged char(1) NULL, 
 	AssetDate smalldatetime NULL, 
 	AssetDateText varchar(25) NULL, 
 	AssetNotes varchar(100) NULL, 
    Dupe char(1) NULL ) ON PRIMARY 
 
CREATE TABLE dbo.Compensation( 
 	ID varchar(15) NOT NULL, 
 	Chamber char(1) NULL, 
 	CID char(9) NULL, 
 	CalendarYear char(2) NULL, 
 	ReportType char(1) NULL, 
 	CompSource varchar(100) NULL, 
 	Orgname varchar(40) NULL, 
 	Ultorg varchar(40) NULL, 
 	Realcode char(5) NULL, 
 	Source char(5) NULL, 
 	CompSourceLocation varchar(50) NULL, 
 	CompDuties varchar(100) NULL, 
 	dupe char(1) NULL 
) ON PRIMARY 
 
CREATE TABLE dbo.Gift( 
    ID varchar(15) NOT NULL, 
    Chamber char(1) NULL, 
    CID char(9) NULL, 
    CalendarYear char(2) NULL, 
    ReportType char(1) NULL, 
    GiftSpouseJointDep char(1) NULL, 
    GiftSource varchar(200) NULL, 
    Orgname varchar(40) NULL, 
    Ultorg varchar(40) NULL, 
    Realcode char(5) NULL, 
    Source char(5) NULL, 
    GiftLocation varchar(50) NULL, 
 	GiftDate smalldatetime NULL, 
 	GiftDateText varchar(20) NULL, 
 	GiftDescrip varchar(200) NULL, 
 	GiftInfo varchar(100) NULL, 
 	GiftValue money NULL, 
 	GiftValueText varchar(50) NULL, 
 	Dupe char(1) NULL 
) ON PRIMARY 
 
CREATE TABLE dbo.Honoraria( 
 	ID varchar(15) NOT NULL, 
 	Chamber char(1) NULL, 
 	CID char(9) NULL, 
 	CalendarYear char(2) NULL, 
 	ReportType char(1) NULL, 
 	HonorariaSource varchar(100) NULL, 
 	Orgname varchar(40) NULL, 
 	Ultorg varchar(40) NULL, 
 	Realcode char(5) NULL, 
 	Source char(5) NULL, 
 	HonorariaSourceLoc varchar(50) NULL, 
 	HonorariaActivity varchar(255) NULL, 
 	HonorariaDate smalldatetime NULL, 
 	HonorariaDateText varchar(20) NULL, 
 	HonorariaAmt money NULL, 
 	HonorariaAmtText varchar(25) NULL, 
 	Dupe char(1) NULL 
) ON PRIMARY 
 
CREATE TABLE dbo.Income( 
 	ID varchar(15) NOT NULL, 
 	Chamber char(1) NULL, 
 	CID char(9) NULL, 
 	CalendarYear char(2) NULL, 
    ReportType char(1) NULL, 
    IncomeSource nvarchar(100) NULL, 
    Orgname varchar(40) NULL, 
    Ultorg varchar(40) NULL, 
    Realcode char(5) NULL, 
    Source char(5) NULL, 
    IncomeLocation varchar(50) NULL, 
    IncomeSpouseDep char(1) NULL, 
    IncomeType varchar(50) NULL, 
    IncomeAmt money NULL, 
    IncomeAmtText varchar(50) NULL, 
    Dupe char(1) NULL ) ON PRIMARY 
 
CREATE TABLE dbo.Liability( 
 	ID varchar(15) NOT NULL, 
 	Chamber char(1) NULL, 
 	CID char(9) NULL, 
 	CalendarYear char(2) NULL, 
 	ReportType char(1) NULL, 
 	LiabilitySpouseJointDep char(1) NULL, 
 	Creditor varchar(100) NULL, 
 	Orgname varchar(40) NULL, 
 	Ultorg varchar(40) NULL, 
 	Realcode char(5) NULL, 
 	Source char(5) NULL, 
 	TypeofLiability varchar(100) NULL, 
 	LiabilityLoc varchar(50) NULL, 
 	LiabilityDate smalldatetime NULL, 
 	LiabilityDateText varchar(25) NULL, 
 	LiabilityTerm varchar(50) NULL, 
 	LiabilityInterestRate varchar(20) NULL, 
 	LiabilityAmt char(2) NULL, 
 	Dupe char(1) NULL 
) ON PRIMARY 
 
CREATE TABLE dbo.Position( 
 	ID varchar(15) NOT NULL, 
 	Chamber char(1) NULL, 
 	CID char(9) NULL, 
 	CalendarYear char(2) NULL, 
 	ReportType char(1) NULL, 
 	PreviousPositions varchar(255) NULL, 
 	PositionHeld varchar(100) NULL, 
 	PositionOrg varchar(100) NULL, 
 	Orgname varchar(40) NULL, 
    Ultorg varchar(40) NULL, 
    Realcode char(5) NULL, 
    Source char(5) NULL, 
    PositionOrgLoc varchar(50) NULL, 
    PositionOrgType varchar(50) NULL, 
    PositionFromDate smalldatetime NULL, 
    PositionFromDateText varchar(50) NULL, 
    PositionToDate smalldatetime NULL, 
    PositionToDateText varchar(50) NULL, 
    Dupe char(1) NULL ) ON PRIMARY 
 
CREATE TABLE dbo.Transactions( 
 	ID varchar(15) NOT NULL, 
 	Chamber char(1) NULL, 
 	CID char(9) NULL, 
 	CalendarYear char(2) NOT NULL, 
 	ReportType char(1) NULL, 
 	Asset4SJD char(1) NULL, 
 	Asset4Transacted varchar(100) NULL, 
 	Orgname varchar(40) NULL, 
 	Ultorg varchar(40) NULL, 
 	Realcode char(5) NULL, 
 	Source char(5) NULL, 
 	Asset4Descrip varchar(100) NULL, 
 	Orgname2 varchar(40) NULL, 
 	Ultorg2 varchar(40) NULL, 
 	Realcode2 char(5) NULL, 
 	Source2 char(5) NULL, 
 	Asset4Purchased char(1) NULL, 
 	Asset4Sold char(1) NULL, 
 	Asset4Exchanged char(1) NULL, 
 	Asset4Date smalldatetime NULL, 
 	Asset4DateText varchar(50) NULL, 
 	Asset4TransAmt char(2) NULL, 
 	Asset4ExactAmt decimal(18, 0) NULL, 
 	CofD char(1) NULL, 
 	TransNotes varchar(100) NULL, 
 Dupe char(1) NULL ) ON PRIMARY 
 
 
CREATE TABLE dbo.Travel( 
 	ID varchar(15) NOT NULL, 
 	Chamber char(1) NULL, 
 	CID char(9) NULL, 
 	CalendarYear char(2) NULL, 
 	ReportType char(1) NULL, 
 	TravelSource varchar(100) NULL, 
 	Orgname varchar(40) NULL, 
    Ultorg varchar(40) NULL, 
    Realcode char(5) NULL, 
    Source char(5) NULL, 
    SourceCity varchar(50) NULL, 
    SourceState varchar(2) NULL, 
    BeginDate smalldatetime NULL, 
 	BeginDateText varchar(25) NULL, 
 	EndDate smalldatetime NULL, 
 	EndDateText varchar(25) NULL, 
 	DepartCity varchar(50) NULL, 
 	DepartState char(2) NULL, 
 	DestCity varchar(50) NULL, 
 	DestState char(2) NULL, 
 	PofRCity varchar(50) NULL, 
 	PofRState char(2) NULL, 
 	Descrip varchar(255) NULL, 
 	Lodging char(1) NULL, 
 	Food char(1) NULL, 
 	FamilyIncl char(1) NULL, 
 	TimeAtOwnExpense varchar(25) NULL, 
 	Dupe char(1) NULL 
) ON PRIMARY 

--527

CREATE TABLE dbo.Cmtes527( 
 	Cycle char(4) NULL, 
 	Rpt char(4) NULL, 
 	EIN char(9) NOT NULL, 
 	CRP527Name varchar(40) NULL, 
 	Affiliate varchar(40) NULL, 
 	UltOrg varchar(40) NULL, 
 	RecipCode char(2) NULL, 
 	CmteID char(9) NULL, 
 	CID char(9) NULL, 
 	ECCmteID char(10) NULL, 
 	Party char(1) NULL, 
 	PrimCode char(5) NULL, 
 	Source char(10) NULL, 
 	FFreq char(1) NULL, 
 	Ctype char(10) NULL, 
 	CSource char(5) NULL, 
 	ViewPt char(1) NULL, 
 	Comments char(250) NULL, 
 	State char(2) NULL 
) ON PRIMARY 

CREATE TABLE dbo.receipts527( 
 	ID int NOT NULL, 
 	Rpt char(4) NULL, 
 	FormID varchar(38) NULL, 
 	SchAID varchar(38) NULL, 
 	ContribID char(12) NULL, 
 	Contrib varchar(50) NULL, 
 	Amount int NULL, 
 	Date smalldatetime NULL, 
 	Orgname varchar(50) NULL, 
 	Ultorg varchar(50) NULL, 
 	Realcode char(5) NULL, 
 	RecipID char(9) NULL, 
 	RecipCode char(2) NULL, 
 	Party char(1) NULL, 
 	Recipient varchar(50) NULL, 
 	City varchar(50) NULL, 
 	State char(2) NULL, 
 	Zip char(5) NULL, 
 	Zip4 char(4) NULL, 
 	PMSA char(4) NULL, 
 	Employer varchar(70) NULL,  	
    Occupation varchar(70) NULL, 
 	YTD varchar(17) NULL, 
 	Gender char(1) NULL, Source char(5) NULL 
) ON PRIMARY 
 
CREATE TABLE dbo.Expenditures527( 
 	Rpt char(4) NULL, 
 	FormID varchar(38) NULL, 
 	SchBID varchar(38) NULL, 
 	Orgname varchar(70) NULL, 
 	EIN char(9) NULL, 
 	Recipient varchar(50) NULL, 
 	RecipientCRP varchar(50) NULL, 
 	Amount int NULL, 
 	Date smalldatetime NULL, 
 	ExpCode char(3) NULL, 
 	Source char(5) NULL, 
 	Purpose varchar(512) NULL, 
 	Addr1 varchar(50) NULL, 
 	Addr2 varchar(50) NULL, 
 	City varchar(50) NULL, 
 	State char(2) NULL, 
 	Zip char(5) NULL, 
 	Employer varchar(70) NULL, 
 	Occupation varchar(70) NULL 
) ON PRIMARY 
