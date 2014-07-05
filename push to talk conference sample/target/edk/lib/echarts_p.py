### $ANTLR 2.7.6 (2005-12-22): "echarts.g" -> "echarts_p.py"$
### import antlr and other modules ..
import sys
import antlr

version = sys.version.split()[0]
if version < '2.2.1':
    False = 0
if version < '2.3':
    True = not False
### header action >>> 

### header action <<< 
### preamble action>>>

### preamble action <<<

### import antlr.Token 
from antlr import Token
### >>>The Known Token Types <<<
SKIP                = antlr.SKIP
INVALID_TYPE        = antlr.INVALID_TYPE
EOF_TYPE            = antlr.EOF_TYPE
EOF                 = antlr.EOF
NULL_TREE_LOOKAHEAD = antlr.NULL_TREE_LOOKAHEAD
MIN_USER_TYPE       = antlr.MIN_USER_TYPE
BLOCK = 4
ACCESS_MODIFIERS = 5
OBJBLOCK = 6
MACHINE_BODY = 7
STATE_DEF = 8
TRANSITION_DEF = 9
ACTION_BLOCK = 10
HOST_BLOCK = 11
SRC_CONFIG = 12
TGT_CONFIG = 13
PORT_SEND = 14
EXPR = 15
PORT_REF = 16
PORT_RECEIVE = 17
GUARD = 18
COMPILATION_UNIT = 19
HOST = 20
IMPLEMENTS_CLAUSE = 21
STATE_MODIFIERS = 22
MACHINE_MODIFIERS = 23
EXTERNAL = 24
NO_SUBMACHINE = 25
STATES = 26
TRANSITIONS = 27
ENTRY = 28
EXIT = 29
INNER_SUBMACHINE = 30
EXTERNAL_SUBMACHINE = 31
VARIABLE_SUBMACHINE = 32
TRANSITION_ACTION = 33
BASIC_CONFIG = 34
VARIABLE_CONFIG = 35
DYNAMIC_CONFIG = 36
AND_CONFIG = 37
OR_CONFIG = 38
MULTI_CONFIG = 39
CONSTRUCTORS = 40
ARGUMENTS = 41
CONSTRUCTOR_DEF = 42
SET_INDEX = 43
GET_INDEX = 44
EMPTY_INDEX = 45
REFLECT_SUBMACHINE = 46
MACHINE_DEF = 47
TYPE = 48
ARRAY_INIT = 49
TRANSITION_MODIFIERS = 50
PARAMETERS = 51
PARAMETER_DEF = 52
IMPORT_DEF = 53
PACKAGE_DEF = 54
EXTENDS_CLAUSE = 55
ARRAY_DECLARATOR = 56
ELIST = 57
METHOD_CALL = 58
INDEX_OP = 59
TYPECAST = 60
NEW_EXPRESSION = 61
POST_DEC = 62
POST_INC = 63
UNARY_MINUS = 64
UNARY_PLUS = 65
PRIMARY_EXPRESSION = 66
COMPOUND_TGT = 67
BASIC_TGT = 68
GUARDED_TGT = 69
LINECOLUMN = 70
IMPORTS = 71
IMPORT_MODIFIERS = 72
SEMI = 73
LITERAL_package = 74
LITERAL_import = 75
LITERAL_static = 76
LITERAL_machine = 77
IDENT = 78
LITERAL_extends = 79
LITERAL_implements = 80
COMMA = 81
LITERAL_private = 82
LITERAL_public = 83
LITERAL_protected = 84
LITERAL_final = 85
LITERAL_abstract = 86
LCURLY = 87
RCURLY = 88
LITERAL_state = 89
COLON = 90
LBRACK = 91
RBRACK = 92
LITERAL_initial = 93
LITERAL_nonterminal = 94
LITERAL_concurrent = 95
LITERAL_entry = 96
LITERAL_exit = 97
LPAREN = 98
RPAREN = 99
LITERAL_reflect = 100
LITERAL_transition = 101
MINUS = 102
LITERAL_constport = 103
LITERAL_else = 104
DIV = 105
SMALL_ARROW = 106
DOT = 107
QUESTION = 108
LITERAL_delay = 109
STAR = 110
LNOT = 111
ASSIGN = 112
PLUS_ASSIGN = 113
MINUS_ASSIGN = 114
STAR_ASSIGN = 115
DIV_ASSIGN = 116
MOD_ASSIGN = 117
SR_ASSIGN = 118
BSR_ASSIGN = 119
SL_ASSIGN = 120
BAND_ASSIGN = 121
BXOR_ASSIGN = 122
BOR_ASSIGN = 123
LOR = 124
LAND = 125
BOR = 126
BXOR = 127
BAND = 128
NOT_EQUAL = 129
EQUAL = 130
LT = 131
GT = 132
LE = 133
GE = 134
SL = 135
SR = 136
BSR = 137
PLUS = 138
MOD = 139
INC = 140
DEC = 141
BNOT = 142
LITERAL_new = 143
NUM_INT = 144
CHAR_LITERAL = 145
STRING_LITERAL = 146
NUM_FLOAT = 147
NUM_LONG = 148
NUM_DOUBLE = 149
WS = 150
SL_COMMENT = 151
ML_COMMENT = 152
ESC = 153
HEX_DIGIT = 154
EXPONENT = 155
FLOAT_SUFFIX = 156

class Parser(antlr.LLkParser):
    ### user action >>>
    ### user action <<<
    
    def __init__(self, *args, **kwargs):
        antlr.LLkParser.__init__(self, *args, **kwargs)
        self.tokenNames = _tokenNames
        self.buildTokenTypeASTClassMap()
        self.astFactory = antlr.ASTFactory(self.getTokenTypeToASTClassMap())
        self.astFactory.setASTNodeClass()
        
    def compilationUnit(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        compilationUnit_AST = None
        try:      ## for error handling
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LITERAL_package]:
                pass
                self.packageDefinition()
                self.addASTChild(currentAST, self.returnAST)
                self.match(SEMI)
            elif la1 and la1 in [LITERAL_import,LITERAL_machine,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,LITERAL_concurrent]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            while True:
                if (self.LA(1)==LITERAL_import):
                    pass
                    self.importDefinition()
                    self.addASTChild(currentAST, self.returnAST)
                    self.match(SEMI)
                else:
                    break
                
            self.machineDefinition()
            self.addASTChild(currentAST, self.returnAST)
            self.match(EOF_TYPE)
            compilationUnit_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_0)
            else:
                raise ex
        
        self.returnAST = compilationUnit_AST
    
    def packageDefinition(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        packageDefinition_AST = None
        p = None
        p_AST = None
        try:      ## for error handling
            pass
            p = self.LT(1)
            p_AST = self.astFactory.create(p)
            self.makeASTRoot(currentAST, p_AST)
            self.match(LITERAL_package)
            self.identifier()
            self.addASTChild(currentAST, self.returnAST)
            if not self.inputState.guessing:
                p_AST.setType(PACKAGE_DEF);
            packageDefinition_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_1)
            else:
                raise ex
        
        self.returnAST = packageDefinition_AST
    
    def importDefinition(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        importDefinition_AST = None
        i = None
        i_AST = None
        im_AST = None
        is_AST = None
        try:      ## for error handling
            pass
            i = self.LT(1)
            i_AST = self.astFactory.create(i)
            self.match(LITERAL_import)
            self.importModifiers()
            im_AST = self.returnAST
            self.identifierStar()
            is_AST = self.returnAST
            if not self.inputState.guessing:
                importDefinition_AST = currentAST.root
                i_AST.setType(IMPORT_DEF);
                importDefinition_AST = antlr.make(i_AST, im_AST, is_AST);
                currentAST.root = importDefinition_AST
                if (importDefinition_AST != None) and (importDefinition_AST.getFirstChild() != None):
                    currentAST.child = importDefinition_AST.getFirstChild()
                else:
                    currentAST.child = importDefinition_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_1)
            else:
                raise ex
        
        self.returnAST = importDefinition_AST
    
    def machineDefinition(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        machineDefinition_AST = None
        am_AST = None
        mm_AST = None
        m = None
        m_AST = None
        sc_AST = None
        ic_AST = None
        mb_AST = None
        try:      ## for error handling
            pass
            self.accessModifiers()
            am_AST = self.returnAST
            self.machineModifiers()
            mm_AST = self.returnAST
            m = self.LT(1)
            m_AST = self.astFactory.create(m)
            self.match(LITERAL_machine)
            tmp4_AST = None
            tmp4_AST = self.astFactory.create(self.LT(1))
            self.match(IDENT)
            self.superClassClause()
            sc_AST = self.returnAST
            self.implementsClause()
            ic_AST = self.returnAST
            self.machineBody()
            mb_AST = self.returnAST
            if not self.inputState.guessing:
                machineDefinition_AST = currentAST.root
                m_AST.setType(MACHINE_DEF); 
                machineDefinition_AST = antlr.make(m_AST, am_AST, mm_AST, tmp4_AST, sc_AST, ic_AST, mb_AST);
                currentAST.root = machineDefinition_AST
                if (machineDefinition_AST != None) and (machineDefinition_AST.getFirstChild() != None):
                    currentAST.child = machineDefinition_AST.getFirstChild()
                else:
                    currentAST.child = machineDefinition_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_0)
            else:
                raise ex
        
        self.returnAST = machineDefinition_AST
    
    def identifier(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        identifier_AST = None
        try:      ## for error handling
            pass
            tmp5_AST = None
            tmp5_AST = self.astFactory.create(self.LT(1))
            self.addASTChild(currentAST, tmp5_AST)
            self.match(IDENT)
            while True:
                if (self.LA(1)==DOT):
                    pass
                    tmp6_AST = None
                    tmp6_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp6_AST)
                    self.match(DOT)
                    tmp7_AST = None
                    tmp7_AST = self.astFactory.create(self.LT(1))
                    self.addASTChild(currentAST, tmp7_AST)
                    self.match(IDENT)
                else:
                    break
                
            identifier_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_2)
            else:
                raise ex
        
        self.returnAST = identifier_AST
    
    def importModifiers(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        importModifiers_AST = None
        try:      ## for error handling
            pass
            while True:
                if (self.LA(1)==LITERAL_static):
                    pass
                    self.importModifier()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            if not self.inputState.guessing:
                importModifiers_AST = currentAST.root
                importModifiers_AST = antlr.make(self.astFactory.create(IMPORT_MODIFIERS,"IMPORT_MODIFIERS"), importModifiers_AST);
                currentAST.root = importModifiers_AST
                if (importModifiers_AST != None) and (importModifiers_AST.getFirstChild() != None):
                    currentAST.child = importModifiers_AST.getFirstChild()
                else:
                    currentAST.child = importModifiers_AST
                currentAST.advanceChildToEnd()
            importModifiers_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_3)
            else:
                raise ex
        
        self.returnAST = importModifiers_AST
    
    def identifierStar(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        identifierStar_AST = None
        try:      ## for error handling
            pass
            tmp8_AST = None
            tmp8_AST = self.astFactory.create(self.LT(1))
            self.addASTChild(currentAST, tmp8_AST)
            self.match(IDENT)
            while True:
                if (self.LA(1)==DOT) and (self.LA(2)==IDENT):
                    pass
                    tmp9_AST = None
                    tmp9_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp9_AST)
                    self.match(DOT)
                    tmp10_AST = None
                    tmp10_AST = self.astFactory.create(self.LT(1))
                    self.addASTChild(currentAST, tmp10_AST)
                    self.match(IDENT)
                else:
                    break
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [DOT]:
                pass
                tmp11_AST = None
                tmp11_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp11_AST)
                self.match(DOT)
                tmp12_AST = None
                tmp12_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp12_AST)
                self.match(STAR)
            elif la1 and la1 in [SEMI]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            identifierStar_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_1)
            else:
                raise ex
        
        self.returnAST = identifierStar_AST
    
    def importModifier(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        importModifier_AST = None
        try:      ## for error handling
            pass
            tmp13_AST = None
            tmp13_AST = self.astFactory.create(self.LT(1))
            self.addASTChild(currentAST, tmp13_AST)
            self.match(LITERAL_static)
            importModifier_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_4)
            else:
                raise ex
        
        self.returnAST = importModifier_AST
    
    def accessModifiers(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        accessModifiers_AST = None
        try:      ## for error handling
            pass
            while True:
                if ((self.LA(1) >= LITERAL_private and self.LA(1) <= LITERAL_abstract)):
                    pass
                    self.accessModifier()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            if not self.inputState.guessing:
                accessModifiers_AST = currentAST.root
                accessModifiers_AST = antlr.make(self.astFactory.create(ACCESS_MODIFIERS,"ACCESS_MODIFIERS"), accessModifiers_AST);
                currentAST.root = accessModifiers_AST
                if (accessModifiers_AST != None) and (accessModifiers_AST.getFirstChild() != None):
                    currentAST.child = accessModifiers_AST.getFirstChild()
                else:
                    currentAST.child = accessModifiers_AST
                currentAST.advanceChildToEnd()
            accessModifiers_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_5)
            else:
                raise ex
        
        self.returnAST = accessModifiers_AST
    
    def machineModifiers(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        machineModifiers_AST = None
        try:      ## for error handling
            pass
            while True:
                if (self.LA(1)==LITERAL_concurrent):
                    pass
                    self.machineModifier()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            if not self.inputState.guessing:
                machineModifiers_AST = currentAST.root
                machineModifiers_AST = antlr.make(self.astFactory.create(MACHINE_MODIFIERS,"MACHINE_MODIFIERS"), machineModifiers_AST);
                currentAST.root = machineModifiers_AST
                if (machineModifiers_AST != None) and (machineModifiers_AST.getFirstChild() != None):
                    currentAST.child = machineModifiers_AST.getFirstChild()
                else:
                    currentAST.child = machineModifiers_AST
                currentAST.advanceChildToEnd()
            machineModifiers_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_6)
            else:
                raise ex
        
        self.returnAST = machineModifiers_AST
    
    def superClassClause(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        superClassClause_AST = None
        id_AST = None
        try:      ## for error handling
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LITERAL_extends]:
                pass
                self.match(LITERAL_extends)
                self.identifier()
                id_AST = self.returnAST
            elif la1 and la1 in [LITERAL_implements,LCURLY]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            if not self.inputState.guessing:
                superClassClause_AST = currentAST.root
                superClassClause_AST = antlr.make(self.astFactory.create(EXTENDS_CLAUSE,"EXTENDS_CLAUSE"), id_AST);
                currentAST.root = superClassClause_AST
                if (superClassClause_AST != None) and (superClassClause_AST.getFirstChild() != None):
                    currentAST.child = superClassClause_AST.getFirstChild()
                else:
                    currentAST.child = superClassClause_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_7)
            else:
                raise ex
        
        self.returnAST = superClassClause_AST
    
    def implementsClause(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        implementsClause_AST = None
        i = None
        i_AST = None
        try:      ## for error handling
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LITERAL_implements]:
                pass
                i = self.LT(1)
                i_AST = self.astFactory.create(i)
                self.match(LITERAL_implements)
                self.identifier()
                self.addASTChild(currentAST, self.returnAST)
                while True:
                    if (self.LA(1)==COMMA):
                        pass
                        self.match(COMMA)
                        self.identifier()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
            elif la1 and la1 in [LCURLY]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            if not self.inputState.guessing:
                implementsClause_AST = currentAST.root
                implementsClause_AST = antlr.make(self.astFactory.create(IMPLEMENTS_CLAUSE,"IMPLEMENTS_CLAUSE"), implementsClause_AST);
                currentAST.root = implementsClause_AST
                if (implementsClause_AST != None) and (implementsClause_AST.getFirstChild() != None):
                    currentAST.child = implementsClause_AST.getFirstChild()
                else:
                    currentAST.child = implementsClause_AST
                currentAST.advanceChildToEnd()
            implementsClause_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_8)
            else:
                raise ex
        
        self.returnAST = implementsClause_AST
    
    def machineBody(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        machineBody_AST = None
        try:      ## for error handling
            pass
            self.match(LCURLY)
            while True:
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [HOST,IDENT,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,LITERAL_state,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_transition,LITERAL_constport]:
                    pass
                    self.machineStatement()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [SEMI]:
                    pass
                    self.match(SEMI)
                else:
                        break
                    
            self.match(RCURLY)
            if not self.inputState.guessing:
                machineBody_AST = currentAST.root
                machineBody_AST = antlr.make(self.astFactory.create(MACHINE_BODY,"MACHINE_BODY"), machineBody_AST);
                currentAST.root = machineBody_AST
                if (machineBody_AST != None) and (machineBody_AST.getFirstChild() != None):
                    currentAST.child = machineBody_AST.getFirstChild()
                else:
                    currentAST.child = machineBody_AST
                currentAST.advanceChildToEnd()
            machineBody_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_9)
            else:
                raise ex
        
        self.returnAST = machineBody_AST
    
    def accessModifier(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        accessModifier_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LITERAL_private]:
                pass
                tmp19_AST = None
                tmp19_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp19_AST)
                self.match(LITERAL_private)
                accessModifier_AST = currentAST.root
            elif la1 and la1 in [LITERAL_public]:
                pass
                tmp20_AST = None
                tmp20_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp20_AST)
                self.match(LITERAL_public)
                accessModifier_AST = currentAST.root
            elif la1 and la1 in [LITERAL_protected]:
                pass
                tmp21_AST = None
                tmp21_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp21_AST)
                self.match(LITERAL_protected)
                accessModifier_AST = currentAST.root
            elif la1 and la1 in [LITERAL_final]:
                pass
                tmp22_AST = None
                tmp22_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp22_AST)
                self.match(LITERAL_final)
                accessModifier_AST = currentAST.root
            elif la1 and la1 in [LITERAL_abstract]:
                pass
                tmp23_AST = None
                tmp23_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp23_AST)
                self.match(LITERAL_abstract)
                accessModifier_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_10)
            else:
                raise ex
        
        self.returnAST = accessModifier_AST
    
    def machineStatement(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        machineStatement_AST = None
        am_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [IDENT,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,LITERAL_state,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent]:
                pass
                pass
                self.accessModifiers()
                am_AST = self.returnAST
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [LITERAL_state,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent]:
                    pass
                    self.state(am_AST)
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [IDENT]:
                    pass
                    self.machineConstructor(am_AST)
                    self.addASTChild(currentAST, self.returnAST)
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                machineStatement_AST = currentAST.root
            elif la1 and la1 in [LITERAL_transition,LITERAL_constport]:
                pass
                self.transition()
                self.addASTChild(currentAST, self.returnAST)
                machineStatement_AST = currentAST.root
            elif la1 and la1 in [HOST]:
                pass
                self.hostBlock()
                self.addASTChild(currentAST, self.returnAST)
                machineStatement_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_11)
            else:
                raise ex
        
        self.returnAST = machineStatement_AST
    
    def state(self,
        accessMods
    ):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        state_AST = None
        stateMods_AST = None
        s = None
        s_AST = None
        name_AST = None
        en_AST = None
        ex_AST = None
        m_AST = None
        try:      ## for error handling
            pass
            self.stateModifiers()
            stateMods_AST = self.returnAST
            s = self.LT(1)
            s_AST = self.astFactory.create(s)
            self.match(LITERAL_state)
            self.stateName()
            name_AST = self.returnAST
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LITERAL_entry]:
                pass
                self.entry()
                en_AST = self.returnAST
            elif la1 and la1 in [HOST,SEMI,IDENT,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,RCURLY,LITERAL_state,COLON,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_exit,LITERAL_transition,LITERAL_constport]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LITERAL_exit]:
                pass
                self.exit()
                ex_AST = self.returnAST
            elif la1 and la1 in [HOST,SEMI,IDENT,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,RCURLY,LITERAL_state,COLON,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_transition,LITERAL_constport]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [COLON]:
                pass
                self.match(COLON)
                self.submachine()
                m_AST = self.returnAST
            elif la1 and la1 in [HOST,SEMI,IDENT,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,RCURLY,LITERAL_state,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_transition,LITERAL_constport]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            if not self.inputState.guessing:
                state_AST = currentAST.root
                s_AST.setType(STATE_DEF); 
                state_AST = antlr.make(s_AST, accessMods, stateMods_AST, name_AST, en_AST, ex_AST, m_AST);
                currentAST.root = state_AST
                if (state_AST != None) and (state_AST.getFirstChild() != None):
                    currentAST.child = state_AST.getFirstChild()
                else:
                    currentAST.child = state_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_11)
            else:
                raise ex
        
        self.returnAST = state_AST
    
    def machineConstructor(self,
        accessMods
    ):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        machineConstructor_AST = None
        cpl_AST = None
        ab_AST = None
        try:      ## for error handling
            pass
            tmp25_AST = None
            tmp25_AST = self.astFactory.create(self.LT(1))
            self.match(IDENT)
            self.match(LPAREN)
            self.constructorParamList()
            cpl_AST = self.returnAST
            self.match(RPAREN)
            self.actionBlock()
            ab_AST = self.returnAST
            if not self.inputState.guessing:
                machineConstructor_AST = currentAST.root
                machineConstructor_AST = antlr.make(self.astFactory.create(CONSTRUCTOR_DEF,"CONSTRUCTOR_DEF"), accessMods, tmp25_AST, cpl_AST, ab_AST);
                currentAST.root = machineConstructor_AST
                if (machineConstructor_AST != None) and (machineConstructor_AST.getFirstChild() != None):
                    currentAST.child = machineConstructor_AST.getFirstChild()
                else:
                    currentAST.child = machineConstructor_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_11)
            else:
                raise ex
        
        self.returnAST = machineConstructor_AST
    
    def transition(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        transition_AST = None
        transitionMods_AST = None
        t = None
        t_AST = None
        src_AST = None
        r_AST = None
        cxn_AST = None
        try:      ## for error handling
            pass
            self.transitionModifiers()
            transitionMods_AST = self.returnAST
            t = self.LT(1)
            t_AST = self.astFactory.create(t)
            self.match(LITERAL_transition)
            self.srcStateConfig()
            src_AST = self.returnAST
            self.match(MINUS)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [HOST,IDENT,LPAREN,MINUS,LITERAL_delay,STAR,LNOT,PLUS,INC,DEC,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                self.portReceive()
                r_AST = self.returnAST
            elif la1 and la1 in [SEMI,LCURLY,LBRACK,DIV,SMALL_ARROW]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            self.transitionTargets()
            cxn_AST = self.returnAST
            if not self.inputState.guessing:
                transition_AST = currentAST.root
                t_AST.setType(TRANSITION_DEF); 
                transition_AST = antlr.make(t_AST, transitionMods_AST, antlr.make(self.astFactory.create(SRC_CONFIG,"SRC_CONFIG"), src_AST), r_AST, cxn_AST);
                currentAST.root = transition_AST
                if (transition_AST != None) and (transition_AST.getFirstChild() != None):
                    currentAST.child = transition_AST.getFirstChild()
                else:
                    currentAST.child = transition_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_11)
            else:
                raise ex
        
        self.returnAST = transition_AST
    
    def hostBlock(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        hostBlock_AST = None
        h = None
        h_AST = None
        try:      ## for error handling
            pass
            h = self.LT(1)
            h_AST = self.astFactory.create(h)
            self.match(HOST)
            if not self.inputState.guessing:
                hostBlock_AST = currentAST.root
                hostBlock_AST = antlr.make(self.astFactory.create(HOST_BLOCK,"HOST_BLOCK"), h_AST);
                currentAST.root = hostBlock_AST
                if (hostBlock_AST != None) and (hostBlock_AST.getFirstChild() != None):
                    currentAST.child = hostBlock_AST.getFirstChild()
                else:
                    currentAST.child = hostBlock_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_12)
            else:
                raise ex
        
        self.returnAST = hostBlock_AST
    
    def stateModifiers(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        stateModifiers_AST = None
        try:      ## for error handling
            pass
            while True:
                if ((self.LA(1) >= LITERAL_initial and self.LA(1) <= LITERAL_concurrent)):
                    pass
                    self.stateModifier()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            if not self.inputState.guessing:
                stateModifiers_AST = currentAST.root
                stateModifiers_AST = antlr.make(self.astFactory.create(STATE_MODIFIERS,"STATE_MODIFIERS"), stateModifiers_AST);
                currentAST.root = stateModifiers_AST
                if (stateModifiers_AST != None) and (stateModifiers_AST.getFirstChild() != None):
                    currentAST.child = stateModifiers_AST.getFirstChild()
                else:
                    currentAST.child = stateModifiers_AST
                currentAST.advanceChildToEnd()
            stateModifiers_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_13)
            else:
                raise ex
        
        self.returnAST = stateModifiers_AST
    
    def stateName(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        stateName_AST = None
        lb = None
        lb_AST = None
        try:      ## for error handling
            pass
            pass
            tmp29_AST = None
            tmp29_AST = self.astFactory.create(self.LT(1))
            self.addASTChild(currentAST, tmp29_AST)
            self.match(IDENT)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LBRACK]:
                pass
                lb = self.LT(1)
                lb_AST = self.astFactory.create(lb)
                self.addASTChild(currentAST, lb_AST)
                self.match(LBRACK)
                if not self.inputState.guessing:
                    lb_AST.setType(ARRAY_DECLARATOR);
                self.expression()
                self.addASTChild(currentAST, self.returnAST)
                self.match(RBRACK)
            elif la1 and la1 in [HOST,SEMI,IDENT,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,RCURLY,LITERAL_state,COLON,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_entry,LITERAL_exit,LITERAL_transition,LITERAL_constport]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            stateName_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_14)
            else:
                raise ex
        
        self.returnAST = stateName_AST
    
    def entry(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        entry_AST = None
        a_AST = None
        try:      ## for error handling
            pass
            self.match(LITERAL_entry)
            self.action()
            a_AST = self.returnAST
            if not self.inputState.guessing:
                entry_AST = currentAST.root
                entry_AST = antlr.make(self.astFactory.create(ENTRY,"ENTRY"), a_AST);
                currentAST.root = entry_AST
                if (entry_AST != None) and (entry_AST.getFirstChild() != None):
                    currentAST.child = entry_AST.getFirstChild()
                else:
                    currentAST.child = entry_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_15)
            else:
                raise ex
        
        self.returnAST = entry_AST
    
    def exit(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        exit_AST = None
        a_AST = None
        try:      ## for error handling
            pass
            self.match(LITERAL_exit)
            self.action()
            a_AST = self.returnAST
            if not self.inputState.guessing:
                exit_AST = currentAST.root
                exit_AST = antlr.make(self.astFactory.create(EXIT,"EXIT"), a_AST);
                currentAST.root = exit_AST
                if (exit_AST != None) and (exit_AST.getFirstChild() != None):
                    currentAST.child = exit_AST.getFirstChild()
                else:
                    currentAST.child = exit_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_16)
            else:
                raise ex
        
        self.returnAST = exit_AST
    
    def submachine(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        submachine_AST = None
        mm_AST = None
        try:      ## for error handling
            pass
            self.machineModifiers()
            mm_AST = self.returnAST
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LCURLY]:
                pass
                self.innerSubmachine(mm_AST)
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [LITERAL_reflect]:
                pass
                self.reflectSubmachine(mm_AST)
                self.addASTChild(currentAST, self.returnAST)
            else:
                synPredMatched44 = False
                if (self.LA(1)==IDENT) and (self.LA(2)==LPAREN or self.LA(2)==DOT):
                    _m44 = self.mark()
                    synPredMatched44 = True
                    self.inputState.guessing += 1
                    try:
                        pass
                        self.externalSubmachine(mm_AST)
                    except antlr.RecognitionException, pe:
                        synPredMatched44 = False
                    self.rewind(_m44)
                    self.inputState.guessing -= 1
                if synPredMatched44:
                    pass
                    self.externalSubmachine(mm_AST)
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    synPredMatched46 = False
                    if (self.LA(1)==IDENT) and (_tokenSet_17.member(self.LA(2))):
                        _m46 = self.mark()
                        synPredMatched46 = True
                        self.inputState.guessing += 1
                        try:
                            pass
                            self.variableSubmachine(mm_AST)
                        except antlr.RecognitionException, pe:
                            synPredMatched46 = False
                        self.rewind(_m46)
                        self.inputState.guessing -= 1
                    if synPredMatched46:
                        pass
                        self.variableSubmachine(mm_AST)
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
            submachine_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_11)
            else:
                raise ex
        
        self.returnAST = submachine_AST
    
    def expression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expression_AST = None
        try:      ## for error handling
            pass
            self.assignmentExpression()
            self.addASTChild(currentAST, self.returnAST)
            if not self.inputState.guessing:
                expression_AST = currentAST.root
                expression_AST = antlr.make(self.astFactory.create(EXPR,"EXPR"), expression_AST);
                currentAST.root = expression_AST
                if (expression_AST != None) and (expression_AST.getFirstChild() != None):
                    currentAST.child = expression_AST.getFirstChild()
                else:
                    currentAST.child = expression_AST
                currentAST.advanceChildToEnd()
            expression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_18)
            else:
                raise ex
        
        self.returnAST = expression_AST
    
    def stateModifier(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        stateModifier_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LITERAL_initial]:
                pass
                tmp33_AST = None
                tmp33_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp33_AST)
                self.match(LITERAL_initial)
                stateModifier_AST = currentAST.root
            elif la1 and la1 in [LITERAL_nonterminal]:
                pass
                tmp34_AST = None
                tmp34_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp34_AST)
                self.match(LITERAL_nonterminal)
                stateModifier_AST = currentAST.root
            elif la1 and la1 in [LITERAL_concurrent]:
                pass
                tmp35_AST = None
                tmp35_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp35_AST)
                self.match(LITERAL_concurrent)
                stateModifier_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_19)
            else:
                raise ex
        
        self.returnAST = stateModifier_AST
    
    def action(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        action_AST = None
        try:      ## for error handling
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LCURLY]:
                pass
                self.actionBlock()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [HOST,IDENT,LPAREN,MINUS,LNOT,PLUS,INC,DEC,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                self.actionStatement()
                self.addASTChild(currentAST, self.returnAST)
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            action_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_20)
            else:
                raise ex
        
        self.returnAST = action_AST
    
    def innerSubmachine(self,
        machineMods
    ):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        innerSubmachine_AST = None
        mb_AST = None
        try:      ## for error handling
            pass
            self.machineBody()
            mb_AST = self.returnAST
            if not self.inputState.guessing:
                innerSubmachine_AST = currentAST.root
                innerSubmachine_AST = antlr.make(self.astFactory.create(INNER_SUBMACHINE,"INNER_SUBMACHINE"), machineMods, mb_AST);
                currentAST.root = innerSubmachine_AST
                if (innerSubmachine_AST != None) and (innerSubmachine_AST.getFirstChild() != None):
                    currentAST.child = innerSubmachine_AST.getFirstChild()
                else:
                    currentAST.child = innerSubmachine_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_11)
            else:
                raise ex
        
        self.returnAST = innerSubmachine_AST
    
    def externalSubmachine(self,
        machineMods
    ):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        externalSubmachine_AST = None
        i_AST = None
        a_AST = None
        try:      ## for error handling
            pass
            self.identifier()
            i_AST = self.returnAST
            self.match(LPAREN)
            self.argList()
            a_AST = self.returnAST
            self.match(RPAREN)
            if not self.inputState.guessing:
                externalSubmachine_AST = currentAST.root
                externalSubmachine_AST = antlr.make(self.astFactory.create(EXTERNAL_SUBMACHINE,"EXTERNAL_SUBMACHINE"), machineMods, i_AST, a_AST);
                currentAST.root = externalSubmachine_AST
                if (externalSubmachine_AST != None) and (externalSubmachine_AST.getFirstChild() != None):
                    currentAST.child = externalSubmachine_AST.getFirstChild()
                else:
                    currentAST.child = externalSubmachine_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_11)
            else:
                raise ex
        
        self.returnAST = externalSubmachine_AST
    
    def reflectSubmachine(self,
        machineMods
    ):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        reflectSubmachine_AST = None
        h1_AST = None
        h2_AST = None
        try:      ## for error handling
            pass
            self.match(LITERAL_reflect)
            self.match(LPAREN)
            self.expression()
            h1_AST = self.returnAST
            self.match(COMMA)
            self.expression()
            h2_AST = self.returnAST
            self.match(RPAREN)
            if not self.inputState.guessing:
                reflectSubmachine_AST = currentAST.root
                reflectSubmachine_AST = antlr.make(self.astFactory.create(REFLECT_SUBMACHINE,"REFLECT_SUBMACHINE"), machineMods, h1_AST, h2_AST);
                currentAST.root = reflectSubmachine_AST
                if (reflectSubmachine_AST != None) and (reflectSubmachine_AST.getFirstChild() != None):
                    currentAST.child = reflectSubmachine_AST.getFirstChild()
                else:
                    currentAST.child = reflectSubmachine_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_11)
            else:
                raise ex
        
        self.returnAST = reflectSubmachine_AST
    
    def variableSubmachine(self,
        machineMods
    ):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        variableSubmachine_AST = None
        i_AST = None
        try:      ## for error handling
            pass
            self.identifier()
            i_AST = self.returnAST
            if not self.inputState.guessing:
                variableSubmachine_AST = currentAST.root
                variableSubmachine_AST = antlr.make(self.astFactory.create(VARIABLE_SUBMACHINE,"VARIABLE_SUBMACHINE"), machineMods, i_AST);
                currentAST.root = variableSubmachine_AST
                if (variableSubmachine_AST != None) and (variableSubmachine_AST.getFirstChild() != None):
                    currentAST.child = variableSubmachine_AST.getFirstChild()
                else:
                    currentAST.child = variableSubmachine_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_11)
            else:
                raise ex
        
        self.returnAST = variableSubmachine_AST
    
    def machineModifier(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        machineModifier_AST = None
        try:      ## for error handling
            pass
            pass
            tmp42_AST = None
            tmp42_AST = self.astFactory.create(self.LT(1))
            self.addASTChild(currentAST, tmp42_AST)
            self.match(LITERAL_concurrent)
            machineModifier_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_21)
            else:
                raise ex
        
        self.returnAST = machineModifier_AST
    
    def constructorParamList(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        constructorParamList_AST = None
        try:      ## for error handling
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [IDENT]:
                pass
                self.constructorParam()
                self.addASTChild(currentAST, self.returnAST)
                while True:
                    if (self.LA(1)==COMMA):
                        pass
                        self.match(COMMA)
                        self.constructorParam()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
            elif la1 and la1 in [RPAREN]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            if not self.inputState.guessing:
                constructorParamList_AST = currentAST.root
                constructorParamList_AST = antlr.make(self.astFactory.create(PARAMETERS,"PARAMETERS"), constructorParamList_AST);
                currentAST.root = constructorParamList_AST
                if (constructorParamList_AST != None) and (constructorParamList_AST.getFirstChild() != None):
                    currentAST.child = constructorParamList_AST.getFirstChild()
                else:
                    currentAST.child = constructorParamList_AST
                currentAST.advanceChildToEnd()
            constructorParamList_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_22)
            else:
                raise ex
        
        self.returnAST = constructorParamList_AST
    
    def actionBlock(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        actionBlock_AST = None
        try:      ## for error handling
            pass
            self.match(LCURLY)
            while True:
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [HOST,IDENT,LPAREN,MINUS,LNOT,PLUS,INC,DEC,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                    pass
                    synPredMatched114 = False
                    if (_tokenSet_23.member(self.LA(1))) and (_tokenSet_24.member(self.LA(2))):
                        _m114 = self.mark()
                        synPredMatched114 = True
                        self.inputState.guessing += 1
                        try:
                            pass
                            self.portSend()
                            self.match(SEMI)
                        except antlr.RecognitionException, pe:
                            synPredMatched114 = False
                        self.rewind(_m114)
                        self.inputState.guessing -= 1
                    if synPredMatched114:
                        pass
                        self.portSend()
                        self.addASTChild(currentAST, self.returnAST)
                        self.match(SEMI)
                    else:
                        synPredMatched116 = False
                        if (_tokenSet_23.member(self.LA(1))) and (_tokenSet_25.member(self.LA(2))):
                            _m116 = self.mark()
                            synPredMatched116 = True
                            self.inputState.guessing += 1
                            try:
                                pass
                                self.expression()
                                self.match(SEMI)
                            except antlr.RecognitionException, pe:
                                synPredMatched116 = False
                            self.rewind(_m116)
                            self.inputState.guessing -= 1
                        if synPredMatched116:
                            pass
                            self.expression()
                            self.addASTChild(currentAST, self.returnAST)
                            self.match(SEMI)
                        elif (self.LA(1)==HOST) and (_tokenSet_26.member(self.LA(2))):
                            pass
                            self.hostBlock()
                            self.addASTChild(currentAST, self.returnAST)
                        else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                elif la1 and la1 in [SEMI]:
                    pass
                    self.match(SEMI)
                else:
                        break
                    
            self.match(RCURLY)
            if not self.inputState.guessing:
                actionBlock_AST = currentAST.root
                actionBlock_AST = antlr.make(self.astFactory.create(ACTION_BLOCK,"ACTION_BLOCK"), actionBlock_AST);
                currentAST.root = actionBlock_AST
                if (actionBlock_AST != None) and (actionBlock_AST.getFirstChild() != None):
                    currentAST.child = actionBlock_AST.getFirstChild()
                else:
                    currentAST.child = actionBlock_AST
                currentAST.advanceChildToEnd()
            actionBlock_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_20)
            else:
                raise ex
        
        self.returnAST = actionBlock_AST
    
    def constructorParam(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        constructorParam_AST = None
        c_AST = None
        id = None
        id_AST = None
        try:      ## for error handling
            pass
            self.classTypeSpec(True)
            c_AST = self.returnAST
            id = self.LT(1)
            id_AST = self.astFactory.create(id)
            self.match(IDENT)
            if not self.inputState.guessing:
                constructorParam_AST = currentAST.root
                constructorParam_AST = antlr.make(self.astFactory.create(PARAMETER_DEF,"PARAMETER_DEF"), c_AST, id_AST);
                currentAST.root = constructorParam_AST
                if (constructorParam_AST != None) and (constructorParam_AST.getFirstChild() != None):
                    currentAST.child = constructorParam_AST.getFirstChild()
                else:
                    currentAST.child = constructorParam_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_27)
            else:
                raise ex
        
        self.returnAST = constructorParam_AST
    
    def classTypeSpec(self,
        addImagNode
    ):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        classTypeSpec_AST = None
        lb = None
        lb_AST = None
        try:      ## for error handling
            pass
            self.identifier()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==LBRACK) and (self.LA(2)==RBRACK):
                    pass
                    lb = self.LT(1)
                    lb_AST = self.astFactory.create(lb)
                    self.makeASTRoot(currentAST, lb_AST)
                    self.match(LBRACK)
                    if not self.inputState.guessing:
                        lb_AST.setType(ARRAY_DECLARATOR);
                    self.match(RBRACK)
                else:
                    break
                
            if not self.inputState.guessing:
                classTypeSpec_AST = currentAST.root
                if addImagNode :
                   classTypeSpec_AST = antlr.make(self.astFactory.create(TYPE,"TYPE"), classTypeSpec_AST);
                currentAST.root = classTypeSpec_AST
                if (classTypeSpec_AST != None) and (classTypeSpec_AST.getFirstChild() != None):
                    currentAST.child = classTypeSpec_AST.getFirstChild()
                else:
                    currentAST.child = classTypeSpec_AST
                currentAST.advanceChildToEnd()
            classTypeSpec_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_28)
            else:
                raise ex
        
        self.returnAST = classTypeSpec_AST
    
    def argList(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        argList_AST = None
        try:      ## for error handling
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [HOST,IDENT,LPAREN,MINUS,LNOT,PLUS,INC,DEC,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                self.expressionList()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [RPAREN]:
                pass
                if not self.inputState.guessing:
                    argList_AST = currentAST.root
                    argList_AST = self.astFactory.create(ELIST,"ELIST");
                    currentAST.root = argList_AST
                    if (argList_AST != None) and (argList_AST.getFirstChild() != None):
                        currentAST.child = argList_AST.getFirstChild()
                    else:
                        currentAST.child = argList_AST
                    currentAST.advanceChildToEnd()
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            argList_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_22)
            else:
                raise ex
        
        self.returnAST = argList_AST
    
    def transitionModifiers(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        transitionModifiers_AST = None
        try:      ## for error handling
            pass
            while True:
                if (self.LA(1)==LITERAL_constport):
                    pass
                    self.transitionModifier()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            if not self.inputState.guessing:
                transitionModifiers_AST = currentAST.root
                transitionModifiers_AST = antlr.make(self.astFactory.create(TRANSITION_MODIFIERS,"TRANSITION_MODIFIERS"), transitionModifiers_AST);
                currentAST.root = transitionModifiers_AST
                if (transitionModifiers_AST != None) and (transitionModifiers_AST.getFirstChild() != None):
                    currentAST.child = transitionModifiers_AST.getFirstChild()
                else:
                    currentAST.child = transitionModifiers_AST
                currentAST.advanceChildToEnd()
            transitionModifiers_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_29)
            else:
                raise ex
        
        self.returnAST = transitionModifiers_AST
    
    def srcStateConfig(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        srcStateConfig_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [IDENT]:
                pass
                self.simpleSrcStateConfig()
                self.addASTChild(currentAST, self.returnAST)
                srcStateConfig_AST = currentAST.root
            elif la1 and la1 in [LBRACK]:
                pass
                self.srcStateConfigList()
                self.addASTChild(currentAST, self.returnAST)
                srcStateConfig_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_30)
            else:
                raise ex
        
        self.returnAST = srcStateConfig_AST
    
    def portReceive(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        portReceive_AST = None
        p_AST = None
        m_AST = None
        dl = None
        dl_AST = None
        d_AST = None
        s = None
        s_AST = None
        i_AST = None
        try:      ## for error handling
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [HOST,IDENT,LPAREN,MINUS,LNOT,PLUS,INC,DEC,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                self.expression()
                p_AST = self.returnAST
                self.match(QUESTION)
                self.classTypeSpec(True)
                m_AST = self.returnAST
                if not self.inputState.guessing:
                    portReceive_AST = currentAST.root
                    portReceive_AST = antlr.make(self.astFactory.create(PORT_RECEIVE,"PORT_RECEIVE"), p_AST, m_AST);
                    currentAST.root = portReceive_AST
                    if (portReceive_AST != None) and (portReceive_AST.getFirstChild() != None):
                        currentAST.child = portReceive_AST.getFirstChild()
                    else:
                        currentAST.child = portReceive_AST
                    currentAST.advanceChildToEnd()
            elif la1 and la1 in [LITERAL_delay]:
                pass
                dl = self.LT(1)
                dl_AST = self.astFactory.create(dl)
                self.match(LITERAL_delay)
                self.match(LPAREN)
                self.expression()
                d_AST = self.returnAST
                self.match(RPAREN)
                if not self.inputState.guessing:
                    portReceive_AST = currentAST.root
                    portReceive_AST = antlr.make(self.astFactory.create(PORT_RECEIVE,"PORT_RECEIVE"), antlr.make(dl_AST, d_AST));
                    currentAST.root = portReceive_AST
                    if (portReceive_AST != None) and (portReceive_AST.getFirstChild() != None):
                        currentAST.child = portReceive_AST.getFirstChild()
                    else:
                        currentAST.child = portReceive_AST
                    currentAST.advanceChildToEnd()
            elif la1 and la1 in [STAR]:
                pass
                s = self.LT(1)
                s_AST = self.astFactory.create(s)
                self.match(STAR)
                self.match(QUESTION)
                self.classTypeSpec(True)
                i_AST = self.returnAST
                if not self.inputState.guessing:
                    portReceive_AST = currentAST.root
                    portReceive_AST = antlr.make(self.astFactory.create(PORT_RECEIVE,"PORT_RECEIVE"), s_AST, i_AST);
                    currentAST.root = portReceive_AST
                    if (portReceive_AST != None) and (portReceive_AST.getFirstChild() != None):
                        currentAST.child = portReceive_AST.getFirstChild()
                    else:
                        currentAST.child = portReceive_AST
                    currentAST.advanceChildToEnd()
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_31)
            else:
                raise ex
        
        self.returnAST = portReceive_AST
    
    def transitionTargets(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        transitionTargets_AST = None
        try:      ## for error handling
            pass
            self.guardedTransitionTarget()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==LITERAL_else):
                    pass
                    self.match(LITERAL_else)
                    self.guardedTransitionTarget()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            if not self.inputState.guessing:
                transitionTargets_AST = currentAST.root
                transitionTargets_AST = antlr.make(self.astFactory.create(COMPOUND_TGT,"COMPOUND_TGT"), transitionTargets_AST);
                currentAST.root = transitionTargets_AST
                if (transitionTargets_AST != None) and (transitionTargets_AST.getFirstChild() != None):
                    currentAST.child = transitionTargets_AST.getFirstChild()
                else:
                    currentAST.child = transitionTargets_AST
                currentAST.advanceChildToEnd()
            transitionTargets_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_11)
            else:
                raise ex
        
        self.returnAST = transitionTargets_AST
    
    def transitionModifier(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        transitionModifier_AST = None
        try:      ## for error handling
            pass
            tmp55_AST = None
            tmp55_AST = self.astFactory.create(self.LT(1))
            self.addASTChild(currentAST, tmp55_AST)
            self.match(LITERAL_constport)
            transitionModifier_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_32)
            else:
                raise ex
        
        self.returnAST = transitionModifier_AST
    
    def guardedTransitionTarget(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        guardedTransitionTarget_AST = None
        g_AST = None
        cxn_AST = None
        try:      ## for error handling
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LBRACK]:
                pass
                self.guard()
                g_AST = self.returnAST
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [SEMI,LCURLY,DIV,SMALL_ARROW]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [SEMI,DIV,SMALL_ARROW]:
                pass
                self.basicTransitionTarget()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [LCURLY]:
                pass
                self.match(LCURLY)
                self.transitionTargets()
                cxn_AST = self.returnAST
                self.addASTChild(currentAST, self.returnAST)
                self.match(RCURLY)
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            if not self.inputState.guessing:
                guardedTransitionTarget_AST = currentAST.root
                guardedTransitionTarget_AST = antlr.make(self.astFactory.create(GUARDED_TGT,"GUARDED_TGT"), guardedTransitionTarget_AST);
                currentAST.root = guardedTransitionTarget_AST
                if (guardedTransitionTarget_AST != None) and (guardedTransitionTarget_AST.getFirstChild() != None):
                    currentAST.child = guardedTransitionTarget_AST.getFirstChild()
                else:
                    currentAST.child = guardedTransitionTarget_AST
                currentAST.advanceChildToEnd()
            guardedTransitionTarget_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_33)
            else:
                raise ex
        
        self.returnAST = guardedTransitionTarget_AST
    
    def guard(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        guard_AST = None
        g_AST = None
        try:      ## for error handling
            pass
            self.match(LBRACK)
            self.expression()
            g_AST = self.returnAST
            self.match(RBRACK)
            if not self.inputState.guessing:
                guard_AST = currentAST.root
                guard_AST = antlr.make(self.astFactory.create(GUARD,"GUARD"), g_AST);
                currentAST.root = guard_AST
                if (guard_AST != None) and (guard_AST.getFirstChild() != None):
                    currentAST.child = guard_AST.getFirstChild()
                else:
                    currentAST.child = guard_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_34)
            else:
                raise ex
        
        self.returnAST = guard_AST
    
    def basicTransitionTarget(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        basicTransitionTarget_AST = None
        a_AST = None
        tgt_AST = None
        try:      ## for error handling
            pass
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [DIV]:
                pass
                self.match(DIV)
                self.action()
                a_AST = self.returnAST
            elif la1 and la1 in [SEMI,SMALL_ARROW]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            while True:
                if (self.LA(1)==SEMI):
                    pass
                    self.match(SEMI)
                else:
                    break
                
            self.match(SMALL_ARROW)
            self.tgtStateConfig()
            tgt_AST = self.returnAST
            if not self.inputState.guessing:
                basicTransitionTarget_AST = currentAST.root
                basicTransitionTarget_AST = antlr.make(self.astFactory.create(BASIC_TGT,"BASIC_TGT"), a_AST, antlr.make(self.astFactory.create(TGT_CONFIG,"TGT_CONFIG"), tgt_AST));
                currentAST.root = basicTransitionTarget_AST
                if (basicTransitionTarget_AST != None) and (basicTransitionTarget_AST.getFirstChild() != None):
                    currentAST.child = basicTransitionTarget_AST.getFirstChild()
                else:
                    currentAST.child = basicTransitionTarget_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_33)
            else:
                raise ex
        
        self.returnAST = basicTransitionTarget_AST
    
    def tgtStateConfig(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        tgtStateConfig_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [IDENT]:
                pass
                self.simpleTgtStateConfig()
                self.addASTChild(currentAST, self.returnAST)
                tgtStateConfig_AST = currentAST.root
            elif la1 and la1 in [LBRACK]:
                pass
                self.tgtStateConfigList()
                self.addASTChild(currentAST, self.returnAST)
                tgtStateConfig_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_33)
            else:
                raise ex
        
        self.returnAST = tgtStateConfig_AST
    
    def actionStatement(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        actionStatement_AST = None
        try:      ## for error handling
            pass
            synPredMatched121 = False
            if (_tokenSet_23.member(self.LA(1))) and (_tokenSet_24.member(self.LA(2))):
                _m121 = self.mark()
                synPredMatched121 = True
                self.inputState.guessing += 1
                try:
                    pass
                    self.portSend()
                except antlr.RecognitionException, pe:
                    synPredMatched121 = False
                self.rewind(_m121)
                self.inputState.guessing -= 1
            if synPredMatched121:
                pass
                self.portSend()
                self.addASTChild(currentAST, self.returnAST)
            elif (_tokenSet_23.member(self.LA(1))) and (_tokenSet_35.member(self.LA(2))):
                pass
                self.expression()
                self.addASTChild(currentAST, self.returnAST)
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            
            actionStatement_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_20)
            else:
                raise ex
        
        self.returnAST = actionStatement_AST
    
    def simpleTgtStateConfig(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        simpleTgtStateConfig_AST = None
        try:      ## for error handling
            pass
            self.tgtStateReference()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==DOT):
                    pass
                    tmp63_AST = None
                    tmp63_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp63_AST)
                    self.match(DOT)
                    self.tgtStateReference()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            simpleTgtStateConfig_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_36)
            else:
                raise ex
        
        self.returnAST = simpleTgtStateConfig_AST
    
    def tgtStateConfigList(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        tgtStateConfigList_AST = None
        try:      ## for error handling
            pass
            tmp64_AST = None
            tmp64_AST = self.astFactory.create(self.LT(1))
            self.makeASTRoot(currentAST, tmp64_AST)
            self.match(LBRACK)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [RBRACK]:
                pass
                self.match(RBRACK)
            elif la1 and la1 in [IDENT]:
                pass
                self.simpleTgtStateConfig()
                self.addASTChild(currentAST, self.returnAST)
                while True:
                    if (self.LA(1)==COMMA):
                        pass
                        self.match(COMMA)
                        self.simpleTgtStateConfig()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                self.match(RBRACK)
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            tgtStateConfigList_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_33)
            else:
                raise ex
        
        self.returnAST = tgtStateConfigList_AST
    
    def tgtStateReference(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        tgtStateReference_AST = None
        try:      ## for error handling
            pass
            tmp68_AST = None
            tmp68_AST = self.astFactory.create(self.LT(1))
            self.addASTChild(currentAST, tmp68_AST)
            self.match(IDENT)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LBRACK]:
                pass
                self.machineIndex()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [HOST,SEMI,IDENT,COMMA,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,RCURLY,LITERAL_state,COLON,RBRACK,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_transition,LITERAL_constport,LITERAL_else,DOT]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [COLON]:
                pass
                self.machineInstanceIdentifier()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [HOST,SEMI,IDENT,COMMA,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,RCURLY,LITERAL_state,RBRACK,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_transition,LITERAL_constport,LITERAL_else,DOT]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            tgtStateReference_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_37)
            else:
                raise ex
        
        self.returnAST = tgtStateReference_AST
    
    def machineIndex(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        machineIndex_AST = None
        try:      ## for error handling
            pass
            tmp69_AST = None
            tmp69_AST = self.astFactory.create(self.LT(1))
            self.makeASTRoot(currentAST, tmp69_AST)
            self.match(LBRACK)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [QUESTION]:
                pass
                tmp70_AST = None
                tmp70_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp70_AST)
                self.match(QUESTION)
            elif la1 and la1 in [HOST,IDENT,RBRACK,LPAREN,MINUS,LNOT,PLUS,INC,DEC,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [HOST,IDENT,LPAREN,MINUS,LNOT,PLUS,INC,DEC,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                self.expression()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [RBRACK]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            self.match(RBRACK)
            machineIndex_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_38)
            else:
                raise ex
        
        self.returnAST = machineIndex_AST
    
    def machineInstanceIdentifier(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        machineInstanceIdentifier_AST = None
        try:      ## for error handling
            pass
            tmp72_AST = None
            tmp72_AST = self.astFactory.create(self.LT(1))
            self.makeASTRoot(currentAST, tmp72_AST)
            self.match(COLON)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LITERAL_new]:
                pass
                self.newExpression()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [IDENT]:
                pass
                self.identPrimary()
                self.addASTChild(currentAST, self.returnAST)
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            self.match(COLON)
            machineInstanceIdentifier_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_37)
            else:
                raise ex
        
        self.returnAST = machineInstanceIdentifier_AST
    
    def newExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        newExpression_AST = None
        try:      ## for error handling
            pass
            tmp74_AST = None
            tmp74_AST = self.astFactory.create(self.LT(1))
            self.makeASTRoot(currentAST, tmp74_AST)
            self.match(LITERAL_new)
            self.identifier()
            self.addASTChild(currentAST, self.returnAST)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LPAREN]:
                pass
                self.match(LPAREN)
                self.argList()
                self.addASTChild(currentAST, self.returnAST)
                self.match(RPAREN)
            elif la1 and la1 in [LBRACK]:
                pass
                self.newArrayDeclarator()
                self.addASTChild(currentAST, self.returnAST)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [LCURLY]:
                    pass
                    self.arrayInitializer()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [HOST,SEMI,IDENT,COMMA,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,RCURLY,LITERAL_state,COLON,LBRACK,RBRACK,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_exit,RPAREN,LITERAL_transition,MINUS,LITERAL_constport,DIV,SMALL_ARROW,DOT,QUESTION,STAR,LNOT,ASSIGN,PLUS_ASSIGN,MINUS_ASSIGN,STAR_ASSIGN,DIV_ASSIGN,MOD_ASSIGN,SR_ASSIGN,BSR_ASSIGN,SL_ASSIGN,BAND_ASSIGN,BXOR_ASSIGN,BOR_ASSIGN,LOR,LAND,BOR,BXOR,BAND,NOT_EQUAL,EQUAL,LT,GT,LE,GE,SL,SR,BSR,PLUS,MOD,INC,DEC]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            newExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_39)
            else:
                raise ex
        
        self.returnAST = newExpression_AST
    
    def identPrimary(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        identPrimary_AST = None
        id1 = None
        id1_AST = None
        id2 = None
        id2_AST = None
        lp = None
        lp_AST = None
        lbc = None
        lbc_AST = None
        try:      ## for error handling
            pass
            id1 = self.LT(1)
            id1_AST = self.astFactory.create(id1)
            self.addASTChild(currentAST, id1_AST)
            self.match(IDENT)
            while True:
                if (self.LA(1)==DOT) and (self.LA(2)==IDENT):
                    pass
                    tmp77_AST = None
                    tmp77_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp77_AST)
                    self.match(DOT)
                    id2 = self.LT(1)
                    id2_AST = self.astFactory.create(id2)
                    self.addASTChild(currentAST, id2_AST)
                    self.match(IDENT)
                else:
                    break
                
            if (self.LA(1)==LPAREN):
                pass
                lp = self.LT(1)
                lp_AST = self.astFactory.create(lp)
                self.makeASTRoot(currentAST, lp_AST)
                self.match(LPAREN)
                if not self.inputState.guessing:
                    lp_AST.setType(METHOD_CALL);
                self.argList()
                self.addASTChild(currentAST, self.returnAST)
                self.match(RPAREN)
            elif (self.LA(1)==LBRACK) and (self.LA(2)==RBRACK):
                pass
                _cnt191= 0
                while True:
                    if (self.LA(1)==LBRACK) and (self.LA(2)==RBRACK):
                        pass
                        lbc = self.LT(1)
                        lbc_AST = self.astFactory.create(lbc)
                        self.makeASTRoot(currentAST, lbc_AST)
                        self.match(LBRACK)
                        if not self.inputState.guessing:
                            lbc_AST.setType(ARRAY_DECLARATOR);
                        self.match(RBRACK)
                    else:
                        break
                    
                    _cnt191 += 1
                if _cnt191 < 1:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            elif (_tokenSet_39.member(self.LA(1))) and (_tokenSet_40.member(self.LA(2))):
                pass
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            
            identPrimary_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_39)
            else:
                raise ex
        
        self.returnAST = identPrimary_AST
    
    def simpleSrcStateConfig(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        simpleSrcStateConfig_AST = None
        try:      ## for error handling
            pass
            self.srcStateReference()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==DOT):
                    pass
                    tmp80_AST = None
                    tmp80_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp80_AST)
                    self.match(DOT)
                    self.srcStateReference()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            simpleSrcStateConfig_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_41)
            else:
                raise ex
        
        self.returnAST = simpleSrcStateConfig_AST
    
    def srcStateConfigList(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        srcStateConfigList_AST = None
        try:      ## for error handling
            pass
            tmp81_AST = None
            tmp81_AST = self.astFactory.create(self.LT(1))
            self.makeASTRoot(currentAST, tmp81_AST)
            self.match(LBRACK)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [RBRACK]:
                pass
                self.match(RBRACK)
            elif la1 and la1 in [IDENT]:
                pass
                self.simpleSrcStateConfig()
                self.addASTChild(currentAST, self.returnAST)
                while True:
                    if (self.LA(1)==COMMA):
                        pass
                        self.match(COMMA)
                        self.simpleSrcStateConfig()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                self.match(RBRACK)
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            srcStateConfigList_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_30)
            else:
                raise ex
        
        self.returnAST = srcStateConfigList_AST
    
    def srcStateReference(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        srcStateReference_AST = None
        try:      ## for error handling
            pass
            tmp85_AST = None
            tmp85_AST = self.astFactory.create(self.LT(1))
            self.addASTChild(currentAST, tmp85_AST)
            self.match(IDENT)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LBRACK]:
                pass
                self.machineIndex()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [COMMA,RBRACK,MINUS,DOT]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            srcStateReference_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_42)
            else:
                raise ex
        
        self.returnAST = srcStateReference_AST
    
    def portSend(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        portSend_AST = None
        p_AST = None
        m_AST = None
        try:      ## for error handling
            pass
            self.expression()
            p_AST = self.returnAST
            self.match(LNOT)
            self.expression()
            m_AST = self.returnAST
            if not self.inputState.guessing:
                portSend_AST = currentAST.root
                portSend_AST = antlr.make(self.astFactory.create(PORT_SEND,"PORT_SEND"), p_AST, m_AST);
                currentAST.root = portSend_AST
                if (portSend_AST != None) and (portSend_AST.getFirstChild() != None):
                    currentAST.child = portSend_AST.getFirstChild()
                else:
                    currentAST.child = portSend_AST
                currentAST.advanceChildToEnd()
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_20)
            else:
                raise ex
        
        self.returnAST = portSend_AST
    
    def expressionList(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expressionList_AST = None
        try:      ## for error handling
            pass
            self.expression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==COMMA):
                    pass
                    self.match(COMMA)
                    self.expression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            if not self.inputState.guessing:
                expressionList_AST = currentAST.root
                expressionList_AST = antlr.make(self.astFactory.create(ELIST,"ELIST"), expressionList_AST);
                currentAST.root = expressionList_AST
                if (expressionList_AST != None) and (expressionList_AST.getFirstChild() != None):
                    currentAST.child = expressionList_AST.getFirstChild()
                else:
                    currentAST.child = expressionList_AST
                currentAST.advanceChildToEnd()
            expressionList_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_22)
            else:
                raise ex
        
        self.returnAST = expressionList_AST
    
    def assignmentExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        assignmentExpression_AST = None
        try:      ## for error handling
            pass
            self.logicalOrExpression()
            self.addASTChild(currentAST, self.returnAST)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [ASSIGN,PLUS_ASSIGN,MINUS_ASSIGN,STAR_ASSIGN,DIV_ASSIGN,MOD_ASSIGN,SR_ASSIGN,BSR_ASSIGN,SL_ASSIGN,BAND_ASSIGN,BXOR_ASSIGN,BOR_ASSIGN]:
                pass
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [ASSIGN]:
                    pass
                    tmp88_AST = None
                    tmp88_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp88_AST)
                    self.match(ASSIGN)
                elif la1 and la1 in [PLUS_ASSIGN]:
                    pass
                    tmp89_AST = None
                    tmp89_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp89_AST)
                    self.match(PLUS_ASSIGN)
                elif la1 and la1 in [MINUS_ASSIGN]:
                    pass
                    tmp90_AST = None
                    tmp90_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp90_AST)
                    self.match(MINUS_ASSIGN)
                elif la1 and la1 in [STAR_ASSIGN]:
                    pass
                    tmp91_AST = None
                    tmp91_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp91_AST)
                    self.match(STAR_ASSIGN)
                elif la1 and la1 in [DIV_ASSIGN]:
                    pass
                    tmp92_AST = None
                    tmp92_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp92_AST)
                    self.match(DIV_ASSIGN)
                elif la1 and la1 in [MOD_ASSIGN]:
                    pass
                    tmp93_AST = None
                    tmp93_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp93_AST)
                    self.match(MOD_ASSIGN)
                elif la1 and la1 in [SR_ASSIGN]:
                    pass
                    tmp94_AST = None
                    tmp94_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp94_AST)
                    self.match(SR_ASSIGN)
                elif la1 and la1 in [BSR_ASSIGN]:
                    pass
                    tmp95_AST = None
                    tmp95_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp95_AST)
                    self.match(BSR_ASSIGN)
                elif la1 and la1 in [SL_ASSIGN]:
                    pass
                    tmp96_AST = None
                    tmp96_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp96_AST)
                    self.match(SL_ASSIGN)
                elif la1 and la1 in [BAND_ASSIGN]:
                    pass
                    tmp97_AST = None
                    tmp97_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp97_AST)
                    self.match(BAND_ASSIGN)
                elif la1 and la1 in [BXOR_ASSIGN]:
                    pass
                    tmp98_AST = None
                    tmp98_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp98_AST)
                    self.match(BXOR_ASSIGN)
                elif la1 and la1 in [BOR_ASSIGN]:
                    pass
                    tmp99_AST = None
                    tmp99_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp99_AST)
                    self.match(BOR_ASSIGN)
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
                self.assignmentExpression()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [HOST,SEMI,IDENT,COMMA,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,RCURLY,LITERAL_state,COLON,RBRACK,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_exit,RPAREN,LITERAL_transition,LITERAL_constport,SMALL_ARROW,QUESTION,LNOT]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            assignmentExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_18)
            else:
                raise ex
        
        self.returnAST = assignmentExpression_AST
    
    def logicalOrExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        logicalOrExpression_AST = None
        try:      ## for error handling
            pass
            self.logicalAndExpression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==LOR):
                    pass
                    tmp100_AST = None
                    tmp100_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp100_AST)
                    self.match(LOR)
                    self.logicalAndExpression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            logicalOrExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_43)
            else:
                raise ex
        
        self.returnAST = logicalOrExpression_AST
    
    def logicalAndExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        logicalAndExpression_AST = None
        try:      ## for error handling
            pass
            self.inclusiveOrExpression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==LAND):
                    pass
                    tmp101_AST = None
                    tmp101_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp101_AST)
                    self.match(LAND)
                    self.inclusiveOrExpression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            logicalAndExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_44)
            else:
                raise ex
        
        self.returnAST = logicalAndExpression_AST
    
    def inclusiveOrExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        inclusiveOrExpression_AST = None
        try:      ## for error handling
            pass
            self.exclusiveOrExpression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==BOR):
                    pass
                    tmp102_AST = None
                    tmp102_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp102_AST)
                    self.match(BOR)
                    self.exclusiveOrExpression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            inclusiveOrExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_45)
            else:
                raise ex
        
        self.returnAST = inclusiveOrExpression_AST
    
    def exclusiveOrExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        exclusiveOrExpression_AST = None
        try:      ## for error handling
            pass
            self.andExpression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==BXOR):
                    pass
                    tmp103_AST = None
                    tmp103_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp103_AST)
                    self.match(BXOR)
                    self.andExpression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            exclusiveOrExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_46)
            else:
                raise ex
        
        self.returnAST = exclusiveOrExpression_AST
    
    def andExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        andExpression_AST = None
        try:      ## for error handling
            pass
            self.equalityExpression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==BAND):
                    pass
                    tmp104_AST = None
                    tmp104_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp104_AST)
                    self.match(BAND)
                    self.equalityExpression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            andExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_47)
            else:
                raise ex
        
        self.returnAST = andExpression_AST
    
    def equalityExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        equalityExpression_AST = None
        try:      ## for error handling
            pass
            self.relationalExpression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==NOT_EQUAL or self.LA(1)==EQUAL):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [NOT_EQUAL]:
                        pass
                        tmp105_AST = None
                        tmp105_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp105_AST)
                        self.match(NOT_EQUAL)
                    elif la1 and la1 in [EQUAL]:
                        pass
                        tmp106_AST = None
                        tmp106_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp106_AST)
                        self.match(EQUAL)
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.relationalExpression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            equalityExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_48)
            else:
                raise ex
        
        self.returnAST = equalityExpression_AST
    
    def relationalExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        relationalExpression_AST = None
        try:      ## for error handling
            pass
            self.shiftExpression()
            self.addASTChild(currentAST, self.returnAST)
            pass
            while True:
                if ((self.LA(1) >= LT and self.LA(1) <= GE)):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [LT]:
                        pass
                        tmp107_AST = None
                        tmp107_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp107_AST)
                        self.match(LT)
                    elif la1 and la1 in [GT]:
                        pass
                        tmp108_AST = None
                        tmp108_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp108_AST)
                        self.match(GT)
                    elif la1 and la1 in [LE]:
                        pass
                        tmp109_AST = None
                        tmp109_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp109_AST)
                        self.match(LE)
                    elif la1 and la1 in [GE]:
                        pass
                        tmp110_AST = None
                        tmp110_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp110_AST)
                        self.match(GE)
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.shiftExpression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            relationalExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_49)
            else:
                raise ex
        
        self.returnAST = relationalExpression_AST
    
    def shiftExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        shiftExpression_AST = None
        try:      ## for error handling
            pass
            self.additiveExpression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if ((self.LA(1) >= SL and self.LA(1) <= BSR)):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [SL]:
                        pass
                        tmp111_AST = None
                        tmp111_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp111_AST)
                        self.match(SL)
                    elif la1 and la1 in [SR]:
                        pass
                        tmp112_AST = None
                        tmp112_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp112_AST)
                        self.match(SR)
                    elif la1 and la1 in [BSR]:
                        pass
                        tmp113_AST = None
                        tmp113_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp113_AST)
                        self.match(BSR)
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.additiveExpression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            shiftExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_50)
            else:
                raise ex
        
        self.returnAST = shiftExpression_AST
    
    def additiveExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        additiveExpression_AST = None
        try:      ## for error handling
            pass
            self.multiplicativeExpression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==MINUS or self.LA(1)==PLUS):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [PLUS]:
                        pass
                        tmp114_AST = None
                        tmp114_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp114_AST)
                        self.match(PLUS)
                    elif la1 and la1 in [MINUS]:
                        pass
                        tmp115_AST = None
                        tmp115_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp115_AST)
                        self.match(MINUS)
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.multiplicativeExpression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            additiveExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_51)
            else:
                raise ex
        
        self.returnAST = additiveExpression_AST
    
    def multiplicativeExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        multiplicativeExpression_AST = None
        try:      ## for error handling
            pass
            self.unaryExpression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (_tokenSet_52.member(self.LA(1))):
                    pass
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [STAR]:
                        pass
                        tmp116_AST = None
                        tmp116_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp116_AST)
                        self.match(STAR)
                    elif la1 and la1 in [DIV]:
                        pass
                        tmp117_AST = None
                        tmp117_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp117_AST)
                        self.match(DIV)
                    elif la1 and la1 in [MOD]:
                        pass
                        tmp118_AST = None
                        tmp118_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp118_AST)
                        self.match(MOD)
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.unaryExpression()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break
                
            multiplicativeExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_53)
            else:
                raise ex
        
        self.returnAST = multiplicativeExpression_AST
    
    def unaryExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        unaryExpression_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [INC]:
                pass
                tmp119_AST = None
                tmp119_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp119_AST)
                self.match(INC)
                self.unaryExpression()
                self.addASTChild(currentAST, self.returnAST)
                unaryExpression_AST = currentAST.root
            elif la1 and la1 in [DEC]:
                pass
                tmp120_AST = None
                tmp120_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp120_AST)
                self.match(DEC)
                self.unaryExpression()
                self.addASTChild(currentAST, self.returnAST)
                unaryExpression_AST = currentAST.root
            elif la1 and la1 in [MINUS]:
                pass
                tmp121_AST = None
                tmp121_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp121_AST)
                self.match(MINUS)
                if not self.inputState.guessing:
                    tmp121_AST.setType(UNARY_MINUS);
                self.unaryExpression()
                self.addASTChild(currentAST, self.returnAST)
                unaryExpression_AST = currentAST.root
            elif la1 and la1 in [PLUS]:
                pass
                tmp122_AST = None
                tmp122_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp122_AST)
                self.match(PLUS)
                if not self.inputState.guessing:
                    tmp122_AST.setType(UNARY_PLUS);
                self.unaryExpression()
                self.addASTChild(currentAST, self.returnAST)
                unaryExpression_AST = currentAST.root
            elif la1 and la1 in [HOST,IDENT,LPAREN,LNOT,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                self.unaryExpressionNotPlusMinus()
                self.addASTChild(currentAST, self.returnAST)
                unaryExpression_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_54)
            else:
                raise ex
        
        self.returnAST = unaryExpression_AST
    
    def unaryExpressionNotPlusMinus(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        unaryExpressionNotPlusMinus_AST = None
        lp = None
        lp_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [BNOT]:
                pass
                tmp123_AST = None
                tmp123_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp123_AST)
                self.match(BNOT)
                self.unaryExpression()
                self.addASTChild(currentAST, self.returnAST)
                unaryExpressionNotPlusMinus_AST = currentAST.root
            elif la1 and la1 in [LNOT]:
                pass
                tmp124_AST = None
                tmp124_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp124_AST)
                self.match(LNOT)
                self.unaryExpression()
                self.addASTChild(currentAST, self.returnAST)
                unaryExpressionNotPlusMinus_AST = currentAST.root
            else:
                synPredMatched179 = False
                if (self.LA(1)==LPAREN) and (self.LA(2)==IDENT):
                    _m179 = self.mark()
                    synPredMatched179 = True
                    self.inputState.guessing += 1
                    try:
                        pass
                        self.match(LPAREN)
                        self.classTypeSpec(True)
                        self.match(RPAREN)
                        self.unaryExpressionNotPlusMinus()
                    except antlr.RecognitionException, pe:
                        synPredMatched179 = False
                    self.rewind(_m179)
                    self.inputState.guessing -= 1
                if synPredMatched179:
                    pass
                    lp = self.LT(1)
                    lp_AST = self.astFactory.create(lp)
                    self.makeASTRoot(currentAST, lp_AST)
                    self.match(LPAREN)
                    if not self.inputState.guessing:
                        lp_AST.setType(TYPECAST);
                    self.classTypeSpec(True)
                    self.addASTChild(currentAST, self.returnAST)
                    self.match(RPAREN)
                    self.unaryExpressionNotPlusMinus()
                    self.addASTChild(currentAST, self.returnAST)
                    unaryExpressionNotPlusMinus_AST = currentAST.root
                elif (_tokenSet_55.member(self.LA(1))) and (_tokenSet_12.member(self.LA(2))):
                    pass
                    self.postfixExpression()
                    self.addASTChild(currentAST, self.returnAST)
                    unaryExpressionNotPlusMinus_AST = currentAST.root
                else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_54)
            else:
                raise ex
        
        self.returnAST = unaryExpressionNotPlusMinus_AST
    
    def postfixExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        postfixExpression_AST = None
        id = None
        id_AST = None
        lp = None
        lp_AST = None
        lb = None
        lb_AST = None
        inc = None
        inc_AST = None
        dec = None
        dec_AST = None
        try:      ## for error handling
            pass
            self.primaryExpression()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if (self.LA(1)==DOT) and (self.LA(2)==HOST):
                    pass
                    tmp126_AST = None
                    tmp126_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp126_AST)
                    self.match(DOT)
                    self.hostBlock()
                    self.addASTChild(currentAST, self.returnAST)
                elif (self.LA(1)==DOT) and (self.LA(2)==IDENT):
                    pass
                    tmp127_AST = None
                    tmp127_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp127_AST)
                    self.match(DOT)
                    id = self.LT(1)
                    id_AST = self.astFactory.create(id)
                    self.addASTChild(currentAST, id_AST)
                    self.match(IDENT)
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [LPAREN]:
                        pass
                        lp = self.LT(1)
                        lp_AST = self.astFactory.create(lp)
                        self.makeASTRoot(currentAST, lp_AST)
                        self.match(LPAREN)
                        if not self.inputState.guessing:
                            lp_AST.setType(METHOD_CALL);
                        self.argList()
                        self.addASTChild(currentAST, self.returnAST)
                        self.match(RPAREN)
                    elif la1 and la1 in [HOST,SEMI,IDENT,COMMA,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,RCURLY,LITERAL_state,COLON,LBRACK,RBRACK,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_exit,RPAREN,LITERAL_transition,MINUS,LITERAL_constport,DIV,SMALL_ARROW,DOT,QUESTION,STAR,LNOT,ASSIGN,PLUS_ASSIGN,MINUS_ASSIGN,STAR_ASSIGN,DIV_ASSIGN,MOD_ASSIGN,SR_ASSIGN,BSR_ASSIGN,SL_ASSIGN,BAND_ASSIGN,BXOR_ASSIGN,BOR_ASSIGN,LOR,LAND,BOR,BXOR,BAND,NOT_EQUAL,EQUAL,LT,GT,LE,GE,SL,SR,BSR,PLUS,MOD,INC,DEC]:
                        pass
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                elif (self.LA(1)==DOT) and (self.LA(2)==LITERAL_new):
                    pass
                    tmp129_AST = None
                    tmp129_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp129_AST)
                    self.match(DOT)
                    self.newExpression()
                    self.addASTChild(currentAST, self.returnAST)
                elif (self.LA(1)==LBRACK):
                    pass
                    lb = self.LT(1)
                    lb_AST = self.astFactory.create(lb)
                    self.makeASTRoot(currentAST, lb_AST)
                    self.match(LBRACK)
                    if not self.inputState.guessing:
                        lb_AST.setType(INDEX_OP);
                    self.expression()
                    self.addASTChild(currentAST, self.returnAST)
                    self.match(RBRACK)
                else:
                    break
                
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [INC]:
                pass
                inc = self.LT(1)
                inc_AST = self.astFactory.create(inc)
                self.makeASTRoot(currentAST, inc_AST)
                self.match(INC)
                if not self.inputState.guessing:
                    inc_AST.setType(POST_INC);
            elif la1 and la1 in [DEC]:
                pass
                dec = self.LT(1)
                dec_AST = self.astFactory.create(dec)
                self.makeASTRoot(currentAST, dec_AST)
                self.match(DEC)
                if not self.inputState.guessing:
                    dec_AST.setType(POST_DEC);
            elif la1 and la1 in [HOST,SEMI,IDENT,COMMA,LITERAL_private,LITERAL_public,LITERAL_protected,LITERAL_final,LITERAL_abstract,RCURLY,LITERAL_state,COLON,RBRACK,LITERAL_initial,LITERAL_nonterminal,LITERAL_concurrent,LITERAL_exit,RPAREN,LITERAL_transition,MINUS,LITERAL_constport,DIV,SMALL_ARROW,QUESTION,STAR,LNOT,ASSIGN,PLUS_ASSIGN,MINUS_ASSIGN,STAR_ASSIGN,DIV_ASSIGN,MOD_ASSIGN,SR_ASSIGN,BSR_ASSIGN,SL_ASSIGN,BAND_ASSIGN,BXOR_ASSIGN,BOR_ASSIGN,LOR,LAND,BOR,BXOR,BAND,NOT_EQUAL,EQUAL,LT,GT,LE,GE,SL,SR,BSR,PLUS,MOD]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            postfixExpression_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_54)
            else:
                raise ex
        
        self.returnAST = postfixExpression_AST
    
    def primaryExpression(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        primaryExpression_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [HOST]:
                pass
                self.hostBlock()
                self.addASTChild(currentAST, self.returnAST)
                primaryExpression_AST = currentAST.root
            elif la1 and la1 in [IDENT]:
                pass
                self.identPrimary()
                self.addASTChild(currentAST, self.returnAST)
                primaryExpression_AST = currentAST.root
            elif la1 and la1 in [NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                self.constant()
                self.addASTChild(currentAST, self.returnAST)
                primaryExpression_AST = currentAST.root
            elif la1 and la1 in [LITERAL_new]:
                pass
                self.newExpression()
                self.addASTChild(currentAST, self.returnAST)
                primaryExpression_AST = currentAST.root
            elif la1 and la1 in [LPAREN]:
                pass
                self.match(LPAREN)
                self.assignmentExpression()
                self.addASTChild(currentAST, self.returnAST)
                self.match(RPAREN)
                primaryExpression_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_39)
            else:
                raise ex
        
        self.returnAST = primaryExpression_AST
    
    def constant(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        constant_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [NUM_INT]:
                pass
                tmp133_AST = None
                tmp133_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp133_AST)
                self.match(NUM_INT)
                constant_AST = currentAST.root
            elif la1 and la1 in [CHAR_LITERAL]:
                pass
                tmp134_AST = None
                tmp134_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp134_AST)
                self.match(CHAR_LITERAL)
                constant_AST = currentAST.root
            elif la1 and la1 in [STRING_LITERAL]:
                pass
                tmp135_AST = None
                tmp135_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp135_AST)
                self.match(STRING_LITERAL)
                constant_AST = currentAST.root
            elif la1 and la1 in [NUM_FLOAT]:
                pass
                tmp136_AST = None
                tmp136_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp136_AST)
                self.match(NUM_FLOAT)
                constant_AST = currentAST.root
            elif la1 and la1 in [NUM_LONG]:
                pass
                tmp137_AST = None
                tmp137_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp137_AST)
                self.match(NUM_LONG)
                constant_AST = currentAST.root
            elif la1 and la1 in [NUM_DOUBLE]:
                pass
                tmp138_AST = None
                tmp138_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp138_AST)
                self.match(NUM_DOUBLE)
                constant_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_39)
            else:
                raise ex
        
        self.returnAST = constant_AST
    
    def newArrayDeclarator(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        newArrayDeclarator_AST = None
        lb = None
        lb_AST = None
        try:      ## for error handling
            pass
            _cnt200= 0
            while True:
                if (self.LA(1)==LBRACK) and (_tokenSet_56.member(self.LA(2))):
                    pass
                    lb = self.LT(1)
                    lb_AST = self.astFactory.create(lb)
                    self.makeASTRoot(currentAST, lb_AST)
                    self.match(LBRACK)
                    if not self.inputState.guessing:
                        lb_AST.setType(ARRAY_DECLARATOR);
                    la1 = self.LA(1)
                    if False:
                        pass
                    elif la1 and la1 in [HOST,IDENT,LPAREN,MINUS,LNOT,PLUS,INC,DEC,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                        pass
                        self.expression()
                        self.addASTChild(currentAST, self.returnAST)
                    elif la1 and la1 in [RBRACK]:
                        pass
                    else:
                            raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                        
                    self.match(RBRACK)
                else:
                    break
                
                _cnt200 += 1
            if _cnt200 < 1:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            newArrayDeclarator_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_57)
            else:
                raise ex
        
        self.returnAST = newArrayDeclarator_AST
    
    def arrayInitializer(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        arrayInitializer_AST = None
        lc = None
        lc_AST = None
        try:      ## for error handling
            pass
            lc = self.LT(1)
            lc_AST = self.astFactory.create(lc)
            self.makeASTRoot(currentAST, lc_AST)
            self.match(LCURLY)
            if not self.inputState.guessing:
                lc_AST.setType(ARRAY_INIT);
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [HOST,IDENT,LCURLY,LPAREN,MINUS,LNOT,PLUS,INC,DEC,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                self.initializer()
                self.addASTChild(currentAST, self.returnAST)
                while True:
                    if (self.LA(1)==COMMA) and (_tokenSet_58.member(self.LA(2))):
                        pass
                        self.match(COMMA)
                        self.initializer()
                        self.addASTChild(currentAST, self.returnAST)
                    else:
                        break
                    
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [COMMA]:
                    pass
                    self.match(COMMA)
                elif la1 and la1 in [RCURLY]:
                    pass
                else:
                        raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                    
            elif la1 and la1 in [RCURLY]:
                pass
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
            self.match(RCURLY)
            arrayInitializer_AST = currentAST.root
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_39)
            else:
                raise ex
        
        self.returnAST = arrayInitializer_AST
    
    def initializer(self):    
        
        self.returnAST = None
        currentAST = antlr.ASTPair()
        initializer_AST = None
        try:      ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [HOST,IDENT,LPAREN,MINUS,LNOT,PLUS,INC,DEC,BNOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                self.expression()
                self.addASTChild(currentAST, self.returnAST)
                initializer_AST = currentAST.root
            elif la1 and la1 in [LCURLY]:
                pass
                self.arrayInitializer()
                self.addASTChild(currentAST, self.returnAST)
                initializer_AST = currentAST.root
            else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())
                
        
        except antlr.RecognitionException, ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_59)
            else:
                raise ex
        
        self.returnAST = initializer_AST
    
    
    def buildTokenTypeASTClassMap(self):
        self.tokenTypeToASTClassMap = None

_tokenNames = [
    "<0>", 
    "EOF", 
    "<2>", 
    "NULL_TREE_LOOKAHEAD", 
    "BLOCK", 
    "ACCESS_MODIFIERS", 
    "OBJBLOCK", 
    "MACHINE_BODY", 
    "STATE_DEF", 
    "TRANSITION_DEF", 
    "ACTION_BLOCK", 
    "HOST_BLOCK", 
    "SRC_CONFIG", 
    "TGT_CONFIG", 
    "PORT_SEND", 
    "EXPR", 
    "PORT_REF", 
    "PORT_RECEIVE", 
    "GUARD", 
    "COMPILATION_UNIT", 
    "HOST", 
    "IMPLEMENTS_CLAUSE", 
    "STATE_MODIFIERS", 
    "MACHINE_MODIFIERS", 
    "EXTERNAL", 
    "NO_SUBMACHINE", 
    "STATES", 
    "TRANSITIONS", 
    "ENTRY", 
    "EXIT", 
    "INNER_SUBMACHINE", 
    "EXTERNAL_SUBMACHINE", 
    "VARIABLE_SUBMACHINE", 
    "TRANSITION_ACTION", 
    "BASIC_CONFIG", 
    "VARIABLE_CONFIG", 
    "DYNAMIC_CONFIG", 
    "AND_CONFIG", 
    "OR_CONFIG", 
    "MULTI_CONFIG", 
    "CONSTRUCTORS", 
    "ARGUMENTS", 
    "CONSTRUCTOR_DEF", 
    "SET_INDEX", 
    "GET_INDEX", 
    "EMPTY_INDEX", 
    "REFLECT_SUBMACHINE", 
    "MACHINE_DEF", 
    "TYPE", 
    "ARRAY_INIT", 
    "TRANSITION_MODIFIERS", 
    "PARAMETERS", 
    "PARAMETER_DEF", 
    "IMPORT_DEF", 
    "PACKAGE_DEF", 
    "EXTENDS_CLAUSE", 
    "ARRAY_DECLARATOR", 
    "ELIST", 
    "METHOD_CALL", 
    "INDEX_OP", 
    "TYPECAST", 
    "NEW_EXPRESSION", 
    "POST_DEC", 
    "POST_INC", 
    "UNARY_MINUS", 
    "UNARY_PLUS", 
    "PRIMARY_EXPRESSION", 
    "COMPOUND_TGT", 
    "BASIC_TGT", 
    "GUARDED_TGT", 
    "LINECOLUMN", 
    "IMPORTS", 
    "IMPORT_MODIFIERS", 
    "SEMI", 
    "\"package\"", 
    "\"import\"", 
    "\"static\"", 
    "\"machine\"", 
    "IDENT", 
    "\"extends\"", 
    "\"implements\"", 
    "COMMA", 
    "\"private\"", 
    "\"public\"", 
    "\"protected\"", 
    "\"final\"", 
    "\"abstract\"", 
    "LCURLY", 
    "RCURLY", 
    "\"state\"", 
    "COLON", 
    "LBRACK", 
    "RBRACK", 
    "\"initial\"", 
    "\"nonterminal\"", 
    "\"concurrent\"", 
    "\"entry\"", 
    "\"exit\"", 
    "LPAREN", 
    "RPAREN", 
    "\"reflect\"", 
    "\"transition\"", 
    "MINUS", 
    "\"constport\"", 
    "\"else\"", 
    "DIV", 
    "SMALL_ARROW", 
    "DOT", 
    "QUESTION", 
    "\"delay\"", 
    "STAR", 
    "LNOT", 
    "ASSIGN", 
    "PLUS_ASSIGN", 
    "MINUS_ASSIGN", 
    "STAR_ASSIGN", 
    "DIV_ASSIGN", 
    "MOD_ASSIGN", 
    "SR_ASSIGN", 
    "BSR_ASSIGN", 
    "SL_ASSIGN", 
    "BAND_ASSIGN", 
    "BXOR_ASSIGN", 
    "BOR_ASSIGN", 
    "LOR", 
    "LAND", 
    "BOR", 
    "BXOR", 
    "BAND", 
    "NOT_EQUAL", 
    "EQUAL", 
    "LT", 
    "GT", 
    "LE", 
    "GE", 
    "SL", 
    "SR", 
    "BSR", 
    "PLUS", 
    "MOD", 
    "INC", 
    "DEC", 
    "BNOT", 
    "\"new\"", 
    "NUM_INT", 
    "CHAR_LITERAL", 
    "STRING_LITERAL", 
    "NUM_FLOAT", 
    "NUM_LONG", 
    "NUM_DOUBLE", 
    "WS", 
    "SL_COMMENT", 
    "ML_COMMENT", 
    "ESC", 
    "HEX_DIGIT", 
    "EXPONENT", 
    "FLOAT_SUFFIX"
]
    

### generate bit set
def mk_tokenSet_0(): 
    ### var1
    data = [ 2L, 0L, 0L]
    return data
_tokenSet_0 = antlr.BitSet(mk_tokenSet_0())

### generate bit set
def mk_tokenSet_1(): 
    ### var1
    data = [ 0L, 512L, 0L, 0L]
    return data
_tokenSet_1 = antlr.BitSet(mk_tokenSet_1())

### generate bit set
def mk_tokenSet_2(): 
    ### var1
    data = [ 1048576L, 7339763515904L, 0L, 0L]
    return data
_tokenSet_2 = antlr.BitSet(mk_tokenSet_2())

### generate bit set
def mk_tokenSet_3(): 
    ### var1
    data = [ 0L, 16384L, 0L, 0L]
    return data
_tokenSet_3 = antlr.BitSet(mk_tokenSet_3())

### generate bit set
def mk_tokenSet_4(): 
    ### var1
    data = [ 0L, 20480L, 0L, 0L]
    return data
_tokenSet_4 = antlr.BitSet(mk_tokenSet_4())

### generate bit set
def mk_tokenSet_5(): 
    ### var1
    data = [ 0L, 3791675392L, 0L, 0L]
    return data
_tokenSet_5 = antlr.BitSet(mk_tokenSet_5())

### generate bit set
def mk_tokenSet_6(): 
    ### var1
    data = [ 0L, 68727889920L, 0L, 0L]
    return data
_tokenSet_6 = antlr.BitSet(mk_tokenSet_6())

### generate bit set
def mk_tokenSet_7(): 
    ### var1
    data = [ 0L, 8454144L, 0L, 0L]
    return data
_tokenSet_7 = antlr.BitSet(mk_tokenSet_7())

### generate bit set
def mk_tokenSet_8(): 
    ### var1
    data = [ 0L, 8388608L, 0L, 0L]
    return data
_tokenSet_8 = antlr.BitSet(mk_tokenSet_8())

### generate bit set
def mk_tokenSet_9(): 
    ### var1
    data = [ 1048578L, 691011338752L, 0L, 0L]
    return data
_tokenSet_9 = antlr.BitSet(mk_tokenSet_9())

### generate bit set
def mk_tokenSet_10(): 
    ### var1
    data = [ 0L, 3799801856L, 0L, 0L]
    return data
_tokenSet_10 = antlr.BitSet(mk_tokenSet_10())

### generate bit set
def mk_tokenSet_11(): 
    ### var1
    data = [ 1048576L, 691011338752L, 0L, 0L]
    return data
_tokenSet_11 = antlr.BitSet(mk_tokenSet_11())

### generate bit set
def mk_tokenSet_12(): 
    ### var1
    data = [ 1048576L, -36356906663424L, 4194303L, 0L, 0L, 0L]
    return data
_tokenSet_12 = antlr.BitSet(mk_tokenSet_12())

### generate bit set
def mk_tokenSet_13(): 
    ### var1
    data = [ 0L, 33554432L, 0L, 0L]
    return data
_tokenSet_13 = antlr.BitSet(mk_tokenSet_13())

### generate bit set
def mk_tokenSet_14(): 
    ### var1
    data = [ 1048576L, 703963349504L, 0L, 0L]
    return data
_tokenSet_14 = antlr.BitSet(mk_tokenSet_14())

### generate bit set
def mk_tokenSet_15(): 
    ### var1
    data = [ 1048576L, 699668382208L, 0L, 0L]
    return data
_tokenSet_15 = antlr.BitSet(mk_tokenSet_15())

### generate bit set
def mk_tokenSet_16(): 
    ### var1
    data = [ 1048576L, 691078447616L, 0L, 0L]
    return data
_tokenSet_16 = antlr.BitSet(mk_tokenSet_16())

### generate bit set
def mk_tokenSet_17(): 
    ### var1
    data = [ 1048576L, 9487104360960L, 0L, 0L]
    return data
_tokenSet_17 = antlr.BitSet(mk_tokenSet_17())

### generate bit set
def mk_tokenSet_18(): 
    ### var1
    data = [ 1048576L, 163462017597952L, 0L, 0L]
    return data
_tokenSet_18 = antlr.BitSet(mk_tokenSet_18())

### generate bit set
def mk_tokenSet_19(): 
    ### var1
    data = [ 0L, 3791650816L, 0L, 0L]
    return data
_tokenSet_19 = antlr.BitSet(mk_tokenSet_19())

### generate bit set
def mk_tokenSet_20(): 
    ### var1
    data = [ 1048576L, 5097714893312L, 0L, 0L]
    return data
_tokenSet_20 = antlr.BitSet(mk_tokenSet_20())

### generate bit set
def mk_tokenSet_21(): 
    ### var1
    data = [ 0L, 70875373568L, 0L, 0L]
    return data
_tokenSet_21 = antlr.BitSet(mk_tokenSet_21())

### generate bit set
def mk_tokenSet_22(): 
    ### var1
    data = [ 0L, 34359738368L, 0L, 0L]
    return data
_tokenSet_22 = antlr.BitSet(mk_tokenSet_22())

### generate bit set
def mk_tokenSet_23(): 
    ### var1
    data = [ 1048576L, 141029546147840L, 4191232L, 0L, 0L, 0L]
    return data
_tokenSet_23 = antlr.BitSet(mk_tokenSet_23())

### generate bit set
def mk_tokenSet_24(): 
    ### var1
    data = [ 1048576L, -59081435889664L, 4194303L, 0L, 0L, 0L]
    return data
_tokenSet_24 = antlr.BitSet(mk_tokenSet_24())

### generate bit set
def mk_tokenSet_25(): 
    ### var1
    data = [ 1048576L, -59081435889152L, 4194303L, 0L, 0L, 0L]
    return data
_tokenSet_25 = antlr.BitSet(mk_tokenSet_25())

### generate bit set
def mk_tokenSet_26(): 
    ### var1
    data = [ 1048576L, 141029562925568L, 4191232L, 0L, 0L, 0L]
    return data
_tokenSet_26 = antlr.BitSet(mk_tokenSet_26())

### generate bit set
def mk_tokenSet_27(): 
    ### var1
    data = [ 0L, 34359869440L, 0L, 0L]
    return data
_tokenSet_27 = antlr.BitSet(mk_tokenSet_27())

### generate bit set
def mk_tokenSet_28(): 
    ### var1
    data = [ 0L, 6631572128256L, 0L, 0L]
    return data
_tokenSet_28 = antlr.BitSet(mk_tokenSet_28())

### generate bit set
def mk_tokenSet_29(): 
    ### var1
    data = [ 0L, 137438953472L, 0L, 0L]
    return data
_tokenSet_29 = antlr.BitSet(mk_tokenSet_29())

### generate bit set
def mk_tokenSet_30(): 
    ### var1
    data = [ 0L, 274877906944L, 0L, 0L]
    return data
_tokenSet_30 = antlr.BitSet(mk_tokenSet_30())

### generate bit set
def mk_tokenSet_31(): 
    ### var1
    data = [ 0L, 6597212373504L, 0L, 0L]
    return data
_tokenSet_31 = antlr.BitSet(mk_tokenSet_31())

### generate bit set
def mk_tokenSet_32(): 
    ### var1
    data = [ 0L, 687194767360L, 0L, 0L]
    return data
_tokenSet_32 = antlr.BitSet(mk_tokenSet_32())

### generate bit set
def mk_tokenSet_33(): 
    ### var1
    data = [ 1048576L, 1790522966528L, 0L, 0L]
    return data
_tokenSet_33 = antlr.BitSet(mk_tokenSet_33())

### generate bit set
def mk_tokenSet_34(): 
    ### var1
    data = [ 0L, 6597078155776L, 0L, 0L]
    return data
_tokenSet_34 = antlr.BitSet(mk_tokenSet_34())

### generate bit set
def mk_tokenSet_35(): 
    ### var1
    data = [ 1048576L, -53983721012736L, 4194303L, 0L, 0L, 0L]
    return data
_tokenSet_35 = antlr.BitSet(mk_tokenSet_35())

### generate bit set
def mk_tokenSet_36(): 
    ### var1
    data = [ 1048576L, 1790791533056L, 0L, 0L]
    return data
_tokenSet_36 = antlr.BitSet(mk_tokenSet_36())

### generate bit set
def mk_tokenSet_37(): 
    ### var1
    data = [ 1048576L, 10586884555264L, 0L, 0L]
    return data
_tokenSet_37 = antlr.BitSet(mk_tokenSet_37())

### generate bit set
def mk_tokenSet_38(): 
    ### var1
    data = [ 1048576L, 10861829571072L, 0L, 0L]
    return data
_tokenSet_38 = antlr.BitSet(mk_tokenSet_38())

### generate bit set
def mk_tokenSet_39(): 
    ### var1
    data = [ 1048576L, -36374086532608L, 16383L, 0L, 0L, 0L]
    return data
_tokenSet_39 = antlr.BitSet(mk_tokenSet_39())

### generate bit set
def mk_tokenSet_40(): 
    ### var1
    data = [ 1048578L, -35184372203008L, 4194303L, 0L, 0L, 0L]
    return data
_tokenSet_40 = antlr.BitSet(mk_tokenSet_40())

### generate bit set
def mk_tokenSet_41(): 
    ### var1
    data = [ 0L, 275146473472L, 0L, 0L]
    return data
_tokenSet_41 = antlr.BitSet(mk_tokenSet_41())

### generate bit set
def mk_tokenSet_42(): 
    ### var1
    data = [ 0L, 9071239495680L, 0L, 0L]
    return data
_tokenSet_42 = antlr.BitSet(mk_tokenSet_42())

### generate bit set
def mk_tokenSet_43(): 
    ### var1
    data = [ 1048576L, 1152803491647734272L, 0L, 0L]
    return data
_tokenSet_43 = antlr.BitSet(mk_tokenSet_43())

### generate bit set
def mk_tokenSet_44(): 
    ### var1
    data = [ 1048576L, 2305724996254581248L, 0L, 0L]
    return data
_tokenSet_44 = antlr.BitSet(mk_tokenSet_44())

### generate bit set
def mk_tokenSet_45(): 
    ### var1
    data = [ 1048576L, 4611568005468275200L, 0L, 0L]
    return data
_tokenSet_45 = antlr.BitSet(mk_tokenSet_45())

### generate bit set
def mk_tokenSet_46(): 
    ### var1
    data = [ 1048576L, 9223254023895663104L, 0L, 0L]
    return data
_tokenSet_46 = antlr.BitSet(mk_tokenSet_46())

### generate bit set
def mk_tokenSet_47(): 
    ### var1
    data = [ 1048576L, -118012959112704L, 0L, 0L]
    return data
_tokenSet_47 = antlr.BitSet(mk_tokenSet_47())

### generate bit set
def mk_tokenSet_48(): 
    ### var1
    data = [ 1048576L, -118012959112704L, 1L, 0L, 0L, 0L]
    return data
_tokenSet_48 = antlr.BitSet(mk_tokenSet_48())

### generate bit set
def mk_tokenSet_49(): 
    ### var1
    data = [ 1048576L, -118012959112704L, 7L, 0L, 0L, 0L]
    return data
_tokenSet_49 = antlr.BitSet(mk_tokenSet_49())

### generate bit set
def mk_tokenSet_50(): 
    ### var1
    data = [ 1048576L, -118012959112704L, 127L, 0L, 0L, 0L]
    return data
_tokenSet_50 = antlr.BitSet(mk_tokenSet_50())

### generate bit set
def mk_tokenSet_51(): 
    ### var1
    data = [ 1048576L, -118012959112704L, 1023L, 0L, 0L, 0L]
    return data
_tokenSet_51 = antlr.BitSet(mk_tokenSet_51())

### generate bit set
def mk_tokenSet_52(): 
    ### var1
    data = [ 0L, 72567767433216L, 2048L, 0L, 0L, 0L]
    return data
_tokenSet_52 = antlr.BitSet(mk_tokenSet_52())

### generate bit set
def mk_tokenSet_53(): 
    ### var1
    data = [ 1048576L, -117738081205760L, 2047L, 0L, 0L, 0L]
    return data
_tokenSet_53 = antlr.BitSet(mk_tokenSet_53())

### generate bit set
def mk_tokenSet_54(): 
    ### var1
    data = [ 1048576L, -45170313772544L, 4095L, 0L, 0L, 0L]
    return data
_tokenSet_54 = antlr.BitSet(mk_tokenSet_54())

### generate bit set
def mk_tokenSet_55(): 
    ### var1
    data = [ 1048576L, 17179885568L, 4161536L, 0L, 0L, 0L]
    return data
_tokenSet_55 = antlr.BitSet(mk_tokenSet_55())

### generate bit set
def mk_tokenSet_56(): 
    ### var1
    data = [ 1048576L, 141029814583296L, 4191232L, 0L, 0L, 0L]
    return data
_tokenSet_56 = antlr.BitSet(mk_tokenSet_56())

### generate bit set
def mk_tokenSet_57(): 
    ### var1
    data = [ 1048576L, -36374078144000L, 16383L, 0L, 0L, 0L]
    return data
_tokenSet_57 = antlr.BitSet(mk_tokenSet_57())

### generate bit set
def mk_tokenSet_58(): 
    ### var1
    data = [ 1048576L, 141029554536448L, 4191232L, 0L, 0L, 0L]
    return data
_tokenSet_58 = antlr.BitSet(mk_tokenSet_58())

### generate bit set
def mk_tokenSet_59(): 
    ### var1
    data = [ 0L, 16908288L, 0L, 0L]
    return data
_tokenSet_59 = antlr.BitSet(mk_tokenSet_59())
    
