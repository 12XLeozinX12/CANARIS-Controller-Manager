#define MyAppName "CANARIS ™ CM"
#define MyAppPublisher "CANARIS"
#define MyAppExeName "CANARIS CM.exe"
#define MyAppVersion "1.0.0"

[Setup]

AppId={{CANARIS-CM-2026}}

AppName={#MyAppName}

AppVersion={#MyAppVersion}

AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\CANARIS CM

DefaultGroupName=CANARIS CM

DisableProgramGroupPage=yes

OutputDir=..\release

OutputBaseFilename=CANARIS CM Setup

Compression=lzma

SolidCompression=yes

WizardStyle=modern


; SetupIconFile=..\assets\icons\canaris.ico



[Files]

Source: "..\dist\CANARIS CM\CANARIS CM.exe"; DestDir: "{app}"; Flags: ignoreversion

Source: "..\assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]

Name: "{autoprograms}\CANARIS CM"; Filename: "{app}\CANARIS CM.exe"

Name: "{autodesktop}\CANARIS CM"; Filename: "{app}\CANARIS CM.exe"



[Run]

Filename: "{app}\CANARIS CM.exe"; Description: "Abrir CANARIS CM"; Flags: nowait postinstall skipifsilent