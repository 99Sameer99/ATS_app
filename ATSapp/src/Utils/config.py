class VDBSETTINGS:
    OPENAI_KEY = "sk-wwnnwncoewicwocnwoicqnqwopjaspxmpoxk"
    VDB_LOCATION = "/tmp/lancedb"
    VDB_TABLENAME = "ats"
    VDB_DUMMYTEXT = "#######wwwww"
    NUM_TOP_RESUMES = 5


class Config(VDBSETTINGS):
    RESUME_DIR = "resumes"