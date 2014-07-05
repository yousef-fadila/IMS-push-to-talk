### $ANTLR 2.7.6 (2005-12-22): "echarts_w.g" -> "echarts_w.py"$
### import antlr and other modules ..
import sys
import antlr

version = sys.version.split()[0]
if version < '2.2.1':
    False = 0
if version < '2.3':
    True = not False
### header action >>> 
import AbstractMachine
### header action <<< 

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

### user code>>>

### user code<<<

class Walker(antlr.TreeParser):
    
    # ctor ..
    def __init__(self, *args, **kwargs):
        antlr.TreeParser.__init__(self, *args, **kwargs)
        self.tokenNames = _tokenNames
    
    ### user action >>>
    ### user action <<<
    def compilationUnit(self, _t):    
        c = None
        
        compilationUnit_AST_in = None
        if _t != antlr.ASTNULL:
            compilationUnit_AST_in = _t
        try:      ## for error handling
            pass
            p = [ [] ]; i = [ ];
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [PACKAGE_DEF]:
                pass
                p=self.packageDefinition(_t)
                _t = self._retTree
            elif la1 and la1 in [MACHINE_DEF,IMPORT_DEF]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==IMPORT_DEF):
                    pass
                    i1=self.importDefinition(_t)
                    _t = self._retTree
                    i = i + [ i1 ];
                else:
                    break
                
            m=self.machineDefinition(_t)
            _t = self._retTree
            c = [ COMPILATION_UNIT, [ PACKAGE_DEF ] + p, [ IMPORTS ] + i, m ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return c
    
    def packageDefinition(self, _t):    
        p = None
        
        packageDefinition_AST_in = None
        if _t != antlr.ASTNULL:
            packageDefinition_AST_in = _t
        pd = None
        try:      ## for error handling
            pass
            _t6 = _t
            pd = antlr.ifelse(_t == antlr.ASTNULL, None, _t)
            self.match(_t,PACKAGE_DEF)
            _t = _t.getFirstChild()
            i=self.identifier(_t)
            _t = self._retTree
            _t = _t6
            _t = _t.getNextSibling()
            p = [ i, AbstractMachine.getLineColumn([pd]) ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return p
    
    def importDefinition(self, _t):    
        i = None
        
        importDefinition_AST_in = None
        if _t != antlr.ASTNULL:
            importDefinition_AST_in = _t
        id = None
        try:      ## for error handling
            pass
            _t8 = _t
            id = antlr.ifelse(_t == antlr.ASTNULL, None, _t)
            self.match(_t,IMPORT_DEF)
            _t = _t.getFirstChild()
            im=self.importModifiers(_t)
            _t = self._retTree
            i1=self.identifierStar(_t)
            _t = self._retTree
            _t = _t8
            _t = _t.getNextSibling()
            i = [ IMPORT_DEF, i1, AbstractMachine.getText(im), AbstractMachine.getLineColumn([id]) ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return i
    
    def machineDefinition(self, _t):    
        m = None
        
        machineDefinition_AST_in = None
        if _t != antlr.ASTNULL:
            machineDefinition_AST_in = _t
        m = None
        i = None
        try:      ## for error handling
            pass
            _t15 = _t
            m = antlr.ifelse(_t == antlr.ASTNULL, None, _t)
            self.match(_t,MACHINE_DEF)
            _t = _t.getFirstChild()
            am=self.accessModifiers(_t)
            _t = self._retTree
            mm=self.machineModifiers(_t)
            _t = self._retTree
            i = _t
            self.match(_t,IDENT)
            _t = _t.getNextSibling()
            ec=self.extendsClause(_t)
            _t = self._retTree
            ic=self.implementsClause(_t)
            _t = self._retTree
            mb=self.machineBody(_t)
            _t = self._retTree
            _t = _t15
            _t = _t.getNextSibling()
            m = [ MACHINE_DEF, 
                          AbstractMachine.getText(am), 
                          AbstractMachine.getText(mm), 
                          i.getText(), 
                          ec, 
                          ic, 
                          AbstractMachine.getComment( am + mm + [ m ] ), 
                          AbstractMachine.getLineColumn( am + mm + [ m ] ), 
                          mb ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return m
    
    def identifier(self, _t):    
        i = None
        
        identifier_AST_in = None
        if _t != antlr.ASTNULL:
            identifier_AST_in = _t
        i1 = None
        i3 = None
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [IDENT]:
                pass
                i1 = _t
                self.match(_t,IDENT)
                _t = _t.getNextSibling()
                i = [ i1.getText() ];
            elif la1 and la1 in [DOT]:
                pass
                _t154 = _t
                tmp1_AST_in = _t
                self.match(_t,DOT)
                _t = _t.getFirstChild()
                i2=self.identifier(_t)
                _t = self._retTree
                i3 = _t
                self.match(_t,IDENT)
                _t = _t.getNextSibling()
                i = i2 + [ i3.getText() ];
                _t = _t154
                _t = _t.getNextSibling()
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return i
    
    def importModifiers(self, _t):    
        im = None
        
        importModifiers_AST_in = None
        if _t != antlr.ASTNULL:
            importModifiers_AST_in = _t
        try:      ## for error handling
            pass
            im = [ IMPORT_MODIFIERS ] ;
            _t10 = _t
            tmp2_AST_in = _t
            self.match(_t,IMPORT_MODIFIERS)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==LITERAL_static):
                    pass
                    i=self.importModifier(_t)
                    _t = self._retTree
                    im = im + [ i ];
                else:
                    break
                
            _t = _t10
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return im
    
    def identifierStar(self, _t):    
        i = None
        
        identifierStar_AST_in = None
        if _t != antlr.ASTNULL:
            identifierStar_AST_in = _t
        i1 = None
        i3 = None
        i4 = None
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [IDENT]:
                pass
                i1 = _t
                self.match(_t,IDENT)
                _t = _t.getNextSibling()
                i = [ i1.getText() ];
            elif la1 and la1 in [DOT]:
                pass
                _t156 = _t
                tmp3_AST_in = _t
                self.match(_t,DOT)
                _t = _t.getFirstChild()
                i2=self.identifier(_t)
                _t = self._retTree
                if not _t:
                    _t = antlr.ASTNULL
                la1 = _t.getType()
                if False:
                    pass
                elif la1 and la1 in [STAR]:
                    pass
                    i3 = _t
                    self.match(_t,STAR)
                    _t = _t.getNextSibling()
                    i = i2 + [ i3.getText() ];
                elif la1 and la1 in [IDENT]:
                    pass
                    i4 = _t
                    self.match(_t,IDENT)
                    _t = _t.getNextSibling()
                    i = i2 + [ i4.getText() ];
                else:
                        raise antlr.NoViableAltException(_t)
                    
                _t = _t156
                _t = _t.getNextSibling()
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return i
    
    def importModifier(self, _t):    
        im = None
        
        importModifier_AST_in = None
        if _t != antlr.ASTNULL:
            importModifier_AST_in = _t
        i1 = None
        try:      ## for error handling
            pass
            i1 = _t
            self.match(_t,LITERAL_static)
            _t = _t.getNextSibling()
            im = i1 ;
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return im
    
    def accessModifiers(self, _t):    
        am = None
        
        accessModifiers_AST_in = None
        if _t != antlr.ASTNULL:
            accessModifiers_AST_in = _t
        try:      ## for error handling
            pass
            am = [ ACCESS_MODIFIERS ];
            _t17 = _t
            tmp4_AST_in = _t
            self.match(_t,ACCESS_MODIFIERS)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if ((_t.getType() >= LITERAL_private and _t.getType() <= LITERAL_abstract)):
                    pass
                    a=self.accessModifier(_t)
                    _t = self._retTree
                    am = am +  [ a ];
                else:
                    break
                
            _t = _t17
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return am
    
    def machineModifiers(self, _t):    
        mm = None
        
        machineModifiers_AST_in = None
        if _t != antlr.ASTNULL:
            machineModifiers_AST_in = _t
        try:      ## for error handling
            pass
            mm = [ MACHINE_MODIFIERS ];
            _t22 = _t
            tmp5_AST_in = _t
            self.match(_t,MACHINE_MODIFIERS)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==LITERAL_concurrent):
                    pass
                    m=self.machineModifier(_t)
                    _t = self._retTree
                    mm = mm + [ m ];
                else:
                    break
                
            _t = _t22
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return mm
    
    def extendsClause(self, _t):    
        ec = None
        
        extendsClause_AST_in = None
        if _t != antlr.ASTNULL:
            extendsClause_AST_in = _t
        try:      ## for error handling
            pass
            ec = [ EXTENDS_CLAUSE ];
            _t27 = _t
            tmp6_AST_in = _t
            self.match(_t,EXTENDS_CLAUSE)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==IDENT or _t.getType()==DOT):
                    pass
                    e=self.identifier(_t)
                    _t = self._retTree
                    ec = ec + [ e ];
                else:
                    break
                
            _t = _t27
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return ec
    
    def implementsClause(self, _t):    
        ic = None
        
        implementsClause_AST_in = None
        if _t != antlr.ASTNULL:
            implementsClause_AST_in = _t
        try:      ## for error handling
            pass
            ic = [ IMPLEMENTS_CLAUSE ];
            _t31 = _t
            tmp7_AST_in = _t
            self.match(_t,IMPLEMENTS_CLAUSE)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==IDENT or _t.getType()==DOT):
                    pass
                    i=self.identifier(_t)
                    _t = self._retTree
                    ic = ic + [ i ];
                else:
                    break
                
            _t = _t31
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return ic
    
    def machineBody(self, _t):    
        mb = None
        
        machineBody_AST_in = None
        if _t != antlr.ASTNULL:
            machineBody_AST_in = _t
        try:      ## for error handling
            pass
            sd = [ STATES ]; td = [ TRANSITIONS ]; hb = [ HOST ]; mc = [ CONSTRUCTORS ]
            _t35 = _t
            tmp8_AST_in = _t
            self.match(_t,MACHINE_BODY)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                la1 = _t.getType()
                if False:
                    pass
                elif la1 and la1 in [STATE_DEF]:
                    pass
                    s=self.stateDef(_t)
                    _t = self._retTree
                    sd = sd + [ s ];
                elif la1 and la1 in [TRANSITION_DEF]:
                    pass
                    t=self.transitionDef(_t)
                    _t = self._retTree
                    td = td + [ t ];
                elif la1 and la1 in [HOST_BLOCK]:
                    pass
                    h=self.commentedHostBlock(_t)
                    _t = self._retTree
                    hb = hb + [ h ];
                elif la1 and la1 in [CONSTRUCTOR_DEF]:
                    pass
                    c=self.machineConstructor(_t)
                    _t = self._retTree
                    mc = mc + [ c ];
                else:
                        break
                    
            _t = _t35
            _t = _t.getNextSibling()
            mb = [ MACHINE_BODY, sd, td, hb, mc ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return mb
    
    def accessModifier(self, _t):    
        am = None
        
        accessModifier_AST_in = None
        if _t != antlr.ASTNULL:
            accessModifier_AST_in = _t
        a1 = None
        a2 = None
        a3 = None
        a4 = None
        a5 = None
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [LITERAL_private]:
                pass
                a1 = _t
                self.match(_t,LITERAL_private)
                _t = _t.getNextSibling()
                am = a1;
            elif la1 and la1 in [LITERAL_public]:
                pass
                a2 = _t
                self.match(_t,LITERAL_public)
                _t = _t.getNextSibling()
                am = a2;
            elif la1 and la1 in [LITERAL_protected]:
                pass
                a3 = _t
                self.match(_t,LITERAL_protected)
                _t = _t.getNextSibling()
                am = a3;
            elif la1 and la1 in [LITERAL_final]:
                pass
                a4 = _t
                self.match(_t,LITERAL_final)
                _t = _t.getNextSibling()
                am = a4;
            elif la1 and la1 in [LITERAL_abstract]:
                pass
                a5 = _t
                self.match(_t,LITERAL_abstract)
                _t = _t.getNextSibling()
                am = a5;
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return am
    
    def machineModifier(self, _t):    
        mm = None
        
        machineModifier_AST_in = None
        if _t != antlr.ASTNULL:
            machineModifier_AST_in = _t
        m1 = None
        try:      ## for error handling
            pass
            m1 = _t
            self.match(_t,LITERAL_concurrent)
            _t = _t.getNextSibling()
            mm = [ m1 ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return mm
    
    def stateDef(self, _t):    
        sd = None
        
        stateDef_AST_in = None
        if _t != antlr.ASTNULL:
            stateDef_AST_in = _t
        s = None
        try:      ## for error handling
            pass
            en = []; ex = []; sub = [];
            _t46 = _t
            s = antlr.ifelse(_t == antlr.ASTNULL, None, _t)
            self.match(_t,STATE_DEF)
            _t = _t.getFirstChild()
            am=self.accessModifiers(_t)
            _t = self._retTree
            sm=self.stateModifiers(_t)
            _t = self._retTree
            n=self.stateName(_t)
            _t = self._retTree
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [ENTRY]:
                pass
                en=self.entry(_t)
                _t = self._retTree
            elif la1 and la1 in [3,EXIT,INNER_SUBMACHINE,EXTERNAL_SUBMACHINE,VARIABLE_SUBMACHINE,REFLECT_SUBMACHINE]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [EXIT]:
                pass
                ex=self.exit(_t)
                _t = self._retTree
            elif la1 and la1 in [3,INNER_SUBMACHINE,EXTERNAL_SUBMACHINE,VARIABLE_SUBMACHINE,REFLECT_SUBMACHINE]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [INNER_SUBMACHINE,EXTERNAL_SUBMACHINE,VARIABLE_SUBMACHINE,REFLECT_SUBMACHINE]:
                pass
                sub=self.submachine(_t)
                _t = self._retTree
            elif la1 and la1 in [3]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            _t = _t46
            _t = _t.getNextSibling()
            sd = [ STATE_DEF,
                           AbstractMachine.getText(am), 
                           AbstractMachine.getText(sm), 
                           n, 
                           [ ENTRY ] + [ en ], 
                           [ EXIT ] + [ ex ], 
                           AbstractMachine.getComment(am + sm + [ s ]),
                           AbstractMachine.getLineColumn(am + sm + [ s ]),
                           sub ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sd
    
    def transitionDef(self, _t):    
        td = None
        
        transitionDef_AST_in = None
        if _t != antlr.ASTNULL:
            transitionDef_AST_in = _t
        tt = None
        try:      ## for error handling
            pass
            p = [ PORT_RECEIVE, [] ];
            _t75 = _t
            tt = antlr.ifelse(_t == antlr.ASTNULL, None, _t)
            self.match(_t,TRANSITION_DEF)
            _t = _t.getFirstChild()
            tm=self.transitionModifiers(_t)
            _t = self._retTree
            s=self.srcConfig(_t)
            _t = self._retTree
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [PORT_RECEIVE]:
                pass
                p1=self.portReceive(_t)
                _t = self._retTree
                p = [ PORT_RECEIVE, p1 ];
            elif la1 and la1 in [COMPOUND_TGT]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            t=self.targets(_t)
            _t = self._retTree
            _t = _t75
            _t = _t.getNextSibling()
            td = [ TRANSITION_DEF, 
                           AbstractMachine.getText(tm), 
                           s, 
                           t, 
                           p, 
                           AbstractMachine.getComment(tm + [ tt ]),
                           AbstractMachine.getLineColumn(tm + [ tt ])];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return td
    
    def commentedHostBlock(self, _t):    
        chb = None
        
        commentedHostBlock_AST_in = None
        if _t != antlr.ASTNULL:
            commentedHostBlock_AST_in = _t
        h = None
        try:      ## for error handling
            pass
            _t136 = _t
            tmp9_AST_in = _t
            self.match(_t,HOST_BLOCK)
            _t = _t.getFirstChild()
            h = _t
            self.match(_t,HOST)
            _t = _t.getNextSibling()
            _t = _t136
            _t = _t.getNextSibling()
            chb = [ HOST_BLOCK, 
                            h.getText(), 
                            AbstractMachine.getLineColumn([ h ]),
                            AbstractMachine.getComment([ h ])];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return chb
    
    def machineConstructor(self, _t):    
        c = None
        
        machineConstructor_AST_in = None
        if _t != antlr.ASTNULL:
            machineConstructor_AST_in = _t
        i = None
        try:      ## for error handling
            pass
            params = [ PARAMETERS ];
            _t39 = _t
            tmp10_AST_in = _t
            self.match(_t,CONSTRUCTOR_DEF)
            _t = _t.getFirstChild()
            am=self.accessModifiers(_t)
            _t = self._retTree
            i = _t
            self.match(_t,IDENT)
            _t = _t.getNextSibling()
            _t40 = _t
            tmp11_AST_in = _t
            self.match(_t,PARAMETERS)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==PARAMETER_DEF):
                    pass
                    p=self.parameter(_t)
                    _t = self._retTree
                    params = params + [ p ];
                else:
                    break
                
            _t = _t40
            _t = _t.getNextSibling()
            ab=self.actionBlock(_t)
            _t = self._retTree
            _t = _t39
            _t = _t.getNextSibling()
            c = [ CONSTRUCTOR_DEF, 
                          AbstractMachine.getText(am), 
                          i.getText(), 
                          params, 
                          ab, 
                          AbstractMachine.getComment(am + [ i ]),
                          AbstractMachine.getLineColumn(am + [ i ]) ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return c
    
    def parameter(self, _t):    
        p = None
        
        parameter_AST_in = None
        if _t != antlr.ASTNULL:
            parameter_AST_in = _t
        i = None
        try:      ## for error handling
            pass
            _t44 = _t
            tmp12_AST_in = _t
            self.match(_t,PARAMETER_DEF)
            _t = _t.getFirstChild()
            c=self.typeSpec(_t)
            _t = self._retTree
            i = _t
            self.match(_t,IDENT)
            _t = _t.getNextSibling()
            _t = _t44
            _t = _t.getNextSibling()
            p = [ c, i.getText() ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return p
    
    def actionBlock(self, _t):    
        ab = None
        
        actionBlock_AST_in = None
        if _t != antlr.ASTNULL:
            actionBlock_AST_in = _t
        try:      ## for error handling
            pass
            ab = [ ACTION_BLOCK ];
            _t140 = _t
            tmp13_AST_in = _t
            self.match(_t,ACTION_BLOCK)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==HOST_BLOCK or _t.getType()==PORT_SEND or _t.getType()==EXPR):
                    pass
                    asm=self.actionStatement(_t)
                    _t = self._retTree
                    ab = ab +  [ asm ];
                else:
                    break
                
            _t = _t140
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return ab
    
    def typeSpec(self, _t):    
        t = None
        
        typeSpec_AST_in = None
        if _t != antlr.ASTNULL:
            typeSpec_AST_in = _t
        try:      ## for error handling
            pass
            _t148 = _t
            tmp14_AST_in = _t
            self.match(_t,TYPE)
            _t = _t.getFirstChild()
            ts=self.typeSpecArray(_t)
            _t = self._retTree
            _t = _t148
            _t = _t.getNextSibling()
            t = [ TYPE, ts ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return t
    
    def stateModifiers(self, _t):    
        sm = None
        
        stateModifiers_AST_in = None
        if _t != antlr.ASTNULL:
            stateModifiers_AST_in = _t
        try:      ## for error handling
            pass
            sm = [ STATE_MODIFIERS ];
            _t51 = _t
            tmp15_AST_in = _t
            self.match(_t,STATE_MODIFIERS)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if ((_t.getType() >= LITERAL_initial and _t.getType() <= LITERAL_concurrent)):
                    pass
                    s=self.stateModifier(_t)
                    _t = self._retTree
                    sm = sm + [ s ];
                else:
                    break
                
            _t = _t51
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sm
    
    def stateName(self, _t):    
        sn = None
        
        stateName_AST_in = None
        if _t != antlr.ASTNULL:
            stateName_AST_in = _t
        n = None
        try:      ## for error handling
            pass
            pass
            n = _t
            self.match(_t,IDENT)
            _t = _t.getNextSibling()
            sn = [ n.getText() ];
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [ARRAY_DECLARATOR]:
                pass
                tmp16_AST_in = _t
                self.match(_t,ARRAY_DECLARATOR)
                _t = _t.getNextSibling()
                f=self.expression(_t)
                _t = self._retTree
                sn = sn + [ f ];
            elif la1 and la1 in [3,ENTRY,EXIT,INNER_SUBMACHINE,EXTERNAL_SUBMACHINE,VARIABLE_SUBMACHINE,REFLECT_SUBMACHINE]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sn
    
    def entry(self, _t):    
        en = None
        
        entry_AST_in = None
        if _t != antlr.ASTNULL:
            entry_AST_in = _t
        try:      ## for error handling
            pass
            _t56 = _t
            tmp17_AST_in = _t
            self.match(_t,ENTRY)
            _t = _t.getFirstChild()
            en=self.action(_t)
            _t = self._retTree
            _t = _t56
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return en
    
    def exit(self, _t):    
        ex = None
        
        exit_AST_in = None
        if _t != antlr.ASTNULL:
            exit_AST_in = _t
        try:      ## for error handling
            pass
            _t58 = _t
            tmp18_AST_in = _t
            self.match(_t,EXIT)
            _t = _t.getFirstChild()
            ex=self.action(_t)
            _t = self._retTree
            _t = _t58
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return ex
    
    def submachine(self, _t):    
        sm = None
        
        submachine_AST_in = None
        if _t != antlr.ASTNULL:
            submachine_AST_in = _t
        try:      ## for error handling
            pass
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [INNER_SUBMACHINE]:
                pass
                a=self.innerSubmachine(_t)
                _t = self._retTree
                sm = a;
            elif la1 and la1 in [EXTERNAL_SUBMACHINE]:
                pass
                e=self.externalSubmachine(_t)
                _t = self._retTree
                sm = e;
            elif la1 and la1 in [VARIABLE_SUBMACHINE]:
                pass
                v=self.variableSubmachine(_t)
                _t = self._retTree
                sm = v;
            elif la1 and la1 in [REFLECT_SUBMACHINE]:
                pass
                n=self.reflectSubmachine(_t)
                _t = self._retTree
                sm = n;
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sm
    
    def stateModifier(self, _t):    
        sm = None
        
        stateModifier_AST_in = None
        if _t != antlr.ASTNULL:
            stateModifier_AST_in = _t
        s1 = None
        s2 = None
        s3 = None
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [LITERAL_initial]:
                pass
                s1 = _t
                self.match(_t,LITERAL_initial)
                _t = _t.getNextSibling()
                sm = s1;
            elif la1 and la1 in [LITERAL_nonterminal]:
                pass
                s2 = _t
                self.match(_t,LITERAL_nonterminal)
                _t = _t.getNextSibling()
                sm = s2;
            elif la1 and la1 in [LITERAL_concurrent]:
                pass
                s3 = _t
                self.match(_t,LITERAL_concurrent)
                _t = _t.getNextSibling()
                sm = s3;
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return sm
    
    def action(self, _t):    
        a = None
        
        action_AST_in = None
        if _t != antlr.ASTNULL:
            action_AST_in = _t
        try:      ## for error handling
            pass
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [ACTION_BLOCK]:
                pass
                a=self.actionBlock(_t)
                _t = self._retTree
            elif la1 and la1 in [HOST_BLOCK,PORT_SEND,EXPR]:
                pass
                a1=self.actionStatement(_t)
                _t = self._retTree
                a = [ ACTION_BLOCK, a1 ];
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return a
    
    def actionStatement(self, _t):    
        asm = None
        
        actionStatement_AST_in = None
        if _t != antlr.ASTNULL:
            actionStatement_AST_in = _t
        try:      ## for error handling
            pass
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [HOST_BLOCK]:
                pass
                asm=self.hostBlock(_t)
                _t = self._retTree
            elif la1 and la1 in [EXPR]:
                pass
                asm=self.expression(_t)
                _t = self._retTree
            elif la1 and la1 in [PORT_SEND]:
                pass
                asm=self.portSend(_t)
                _t = self._retTree
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return asm
    
    def expression(self, _t):    
        e = None
        
        expression_AST_in = None
        if _t != antlr.ASTNULL:
            expression_AST_in = _t
        try:      ## for error handling
            pass
            _t165 = _t
            tmp19_AST_in = _t
            self.match(_t,EXPR)
            _t = _t.getFirstChild()
            e=self.expr(_t)
            _t = self._retTree
            _t = _t165
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return e
    
    def innerSubmachine(self, _t):    
        asm = None
        
        innerSubmachine_AST_in = None
        if _t != antlr.ASTNULL:
            innerSubmachine_AST_in = _t
        try:      ## for error handling
            pass
            _t67 = _t
            tmp20_AST_in = _t
            self.match(_t,INNER_SUBMACHINE)
            _t = _t.getFirstChild()
            mm=self.machineModifiers(_t)
            _t = self._retTree
            mb=self.machineBody(_t)
            _t = self._retTree
            _t = _t67
            _t = _t.getNextSibling()
            asm = [ INNER_SUBMACHINE, AbstractMachine.getText(mm), mb ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return asm
    
    def externalSubmachine(self, _t):    
        es = None
        
        externalSubmachine_AST_in = None
        if _t != antlr.ASTNULL:
            externalSubmachine_AST_in = _t
        try:      ## for error handling
            pass
            _t69 = _t
            tmp21_AST_in = _t
            self.match(_t,EXTERNAL_SUBMACHINE)
            _t = _t.getFirstChild()
            mm=self.machineModifiers(_t)
            _t = self._retTree
            i=self.identifier(_t)
            _t = self._retTree
            c=self.elist(_t)
            _t = self._retTree
            _t = _t69
            _t = _t.getNextSibling()
            es = [ EXTERNAL_SUBMACHINE, AbstractMachine.getText(mm), i, c ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return es
    
    def variableSubmachine(self, _t):    
        vs = None
        
        variableSubmachine_AST_in = None
        if _t != antlr.ASTNULL:
            variableSubmachine_AST_in = _t
        try:      ## for error handling
            pass
            _t71 = _t
            tmp22_AST_in = _t
            self.match(_t,VARIABLE_SUBMACHINE)
            _t = _t.getFirstChild()
            mm=self.machineModifiers(_t)
            _t = self._retTree
            i=self.identifier(_t)
            _t = self._retTree
            _t = _t71
            _t = _t.getNextSibling()
            vs = [ VARIABLE_SUBMACHINE, AbstractMachine.getText(mm), i ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return vs
    
    def reflectSubmachine(self, _t):    
        ns = None
        
        reflectSubmachine_AST_in = None
        if _t != antlr.ASTNULL:
            reflectSubmachine_AST_in = _t
        try:      ## for error handling
            pass
            _t73 = _t
            tmp23_AST_in = _t
            self.match(_t,REFLECT_SUBMACHINE)
            _t = _t.getFirstChild()
            mm=self.machineModifiers(_t)
            _t = self._retTree
            name=self.expression(_t)
            _t = self._retTree
            args=self.expression(_t)
            _t = self._retTree
            _t = _t73
            _t = _t.getNextSibling()
            ns = [ REFLECT_SUBMACHINE, AbstractMachine.getText(mm), name, args ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return ns
    
    def elist(self, _t):    
        el = None
        
        elist_AST_in = None
        if _t != antlr.ASTNULL:
            elist_AST_in = _t
        try:      ## for error handling
            pass
            el = [];
            _t161 = _t
            tmp24_AST_in = _t
            self.match(_t,ELIST)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==EXPR):
                    pass
                    e=self.expression(_t)
                    _t = self._retTree
                    el = el + [ e ];
                else:
                    break
                
            _t = _t161
            _t = _t.getNextSibling()
            el = [ ELIST, el ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return el
    
    def transitionModifiers(self, _t):    
        tm = None
        
        transitionModifiers_AST_in = None
        if _t != antlr.ASTNULL:
            transitionModifiers_AST_in = _t
        try:      ## for error handling
            pass
            tm = [ TRANSITION_MODIFIERS ];
            _t78 = _t
            tmp25_AST_in = _t
            self.match(_t,TRANSITION_MODIFIERS)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==LITERAL_constport):
                    pass
                    m=self.transitionModifier(_t)
                    _t = self._retTree
                    tm = tm + [ m ];
                else:
                    break
                
            _t = _t78
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return tm
    
    def srcConfig(self, _t):    
        c = None
        
        srcConfig_AST_in = None
        if _t != antlr.ASTNULL:
            srcConfig_AST_in = _t
        try:      ## for error handling
            pass
            c = [ ];
            _t83 = _t
            tmp26_AST_in = _t
            self.match(_t,SRC_CONFIG)
            _t = _t.getFirstChild()
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [LBRACK]:
                pass
                c1=self.srcListConfig(_t)
                _t = self._retTree
                c = c + c1;
            elif la1 and la1 in [IDENT,DOT]:
                pass
                c2=self.srcSimpleConfig(_t)
                _t = self._retTree
                c = c + [ c2 ];
            else:
                    raise antlr.NoViableAltException(_t)
                
            _t = _t83
            _t = _t.getNextSibling()
            c = [ SRC_CONFIG ] + [[ c, "" ]];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return c
    
    def portReceive(self, _t):    
        pr = None
        
        portReceive_AST_in = None
        if _t != antlr.ASTNULL:
            portReceive_AST_in = _t
        s = None
        try:      ## for error handling
            pass
            _t127 = _t
            tmp27_AST_in = _t
            self.match(_t,PORT_RECEIVE)
            _t = _t.getFirstChild()
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [EXPR]:
                pass
                pass
                p=self.expression(_t)
                _t = self._retTree
                i1=self.typeSpec(_t)
                _t = self._retTree
                pr = [ p , i1 ];
            elif la1 and la1 in [LITERAL_delay]:
                pass
                d=self.delay(_t)
                _t = self._retTree
                pr = d;
            elif la1 and la1 in [STAR]:
                pass
                pass
                s = _t
                self.match(_t,STAR)
                _t = _t.getNextSibling()
                i2=self.typeSpec(_t)
                _t = self._retTree
                pr = [ s.getText(), i2 ];
            else:
                    raise antlr.NoViableAltException(_t)
                
            _t = _t127
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return pr
    
    def targets(self, _t):    
        t = None
        
        targets_AST_in = None
        if _t != antlr.ASTNULL:
            targets_AST_in = _t
        try:      ## for error handling
            pass
            tt = [];
            _t86 = _t
            tmp28_AST_in = _t
            self.match(_t,COMPOUND_TGT)
            _t = _t.getFirstChild()
            th=self.guardedTarget(_t)
            _t = self._retTree
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==GUARDED_TGT):
                    pass
                    tn=self.guardedTarget(_t)
                    _t = self._retTree
                    tt = tt + [ tn ];
                else:
                    break
                
            tl = [ th ] + tt;
            _t = _t86
            _t = _t.getNextSibling()
            t = [ COMPOUND_TGT, tl ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return t
    
    def transitionModifier(self, _t):    
        tm = None
        
        transitionModifier_AST_in = None
        if _t != antlr.ASTNULL:
            transitionModifier_AST_in = _t
        t1 = None
        try:      ## for error handling
            pass
            t1 = _t
            self.match(_t,LITERAL_constport)
            _t = _t.getNextSibling()
            tm = t1;
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return tm
    
    def srcListConfig(self, _t):    
        c = None
        
        srcListConfig_AST_in = None
        if _t != antlr.ASTNULL:
            srcListConfig_AST_in = _t
        try:      ## for error handling
            pass
            c = [];
            _t123 = _t
            tmp29_AST_in = _t
            self.match(_t,LBRACK)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==IDENT or _t.getType()==DOT):
                    pass
                    c1=self.srcSimpleConfig(_t)
                    _t = self._retTree
                    c = c + [ c1 ];
                else:
                    break
                
            _t = _t123
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return c
    
    def srcSimpleConfig(self, _t):    
        c = None
        
        srcSimpleConfig_AST_in = None
        if _t != antlr.ASTNULL:
            srcSimpleConfig_AST_in = _t
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [IDENT]:
                pass
                s=self.stateReference(_t)
                _t = self._retTree
                c = [ s ];
            elif la1 and la1 in [DOT]:
                pass
                _t110 = _t
                tmp30_AST_in = _t
                self.match(_t,DOT)
                _t = _t.getFirstChild()
                s1=self.srcSimpleConfig(_t)
                _t = self._retTree
                s2=self.stateReference(_t)
                _t = self._retTree
                c = s1 + [ s2 ];
                _t = _t110
                _t = _t.getNextSibling()
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return c
    
    def guardedTarget(self, _t):    
        t = None
        
        guardedTarget_AST_in = None
        if _t != antlr.ASTNULL:
            guardedTarget_AST_in = _t
        try:      ## for error handling
            pass
            g = [ GUARD, [] ];
            _t90 = _t
            tmp31_AST_in = _t
            self.match(_t,GUARDED_TGT)
            _t = _t.getFirstChild()
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [GUARD]:
                pass
                g1=self.guard(_t)
                _t = self._retTree
                g = [ GUARD, g1 ];
            elif la1 and la1 in [COMPOUND_TGT,BASIC_TGT]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [BASIC_TGT]:
                pass
                ts=self.basicTarget(_t)
                _t = self._retTree
            elif la1 and la1 in [COMPOUND_TGT]:
                pass
                ts=self.targets(_t)
                _t = self._retTree
            else:
                    raise antlr.NoViableAltException(_t)
                
            _t = _t90
            _t = _t.getNextSibling()
            t = [ GUARDED_TGT, g, ts ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return t
    
    def guard(self, _t):    
        h = None
        
        guard_AST_in = None
        if _t != antlr.ASTNULL:
            guard_AST_in = _t
        try:      ## for error handling
            pass
            _t134 = _t
            tmp32_AST_in = _t
            self.match(_t,GUARD)
            _t = _t.getFirstChild()
            h=self.expression(_t)
            _t = self._retTree
            _t = _t134
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return h
    
    def basicTarget(self, _t):    
        t = None
        
        basicTarget_AST_in = None
        if _t != antlr.ASTNULL:
            basicTarget_AST_in = _t
        try:      ## for error handling
            pass
            a = [ TRANSITION_ACTION, [] ];
            _t94 = _t
            tmp33_AST_in = _t
            self.match(_t,BASIC_TGT)
            _t = _t.getFirstChild()
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [ACTION_BLOCK,HOST_BLOCK,PORT_SEND,EXPR]:
                pass
                a1=self.action(_t)
                _t = self._retTree
                a = [ TRANSITION_ACTION, a1 ];
            elif la1 and la1 in [TGT_CONFIG]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            tgt=self.tgtConfig(_t)
            _t = self._retTree
            _t = _t94
            _t = _t.getNextSibling()
            t = [ BASIC_TGT, a, tgt ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return t
    
    def tgtConfig(self, _t):    
        c = None
        
        tgtConfig_AST_in = None
        if _t != antlr.ASTNULL:
            tgtConfig_AST_in = _t
        try:      ## for error handling
            pass
            c = [ ];
            _t97 = _t
            tmp34_AST_in = _t
            self.match(_t,TGT_CONFIG)
            _t = _t.getFirstChild()
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [LBRACK]:
                pass
                c1=self.tgtListConfig(_t)
                _t = self._retTree
                c = c + c1;
            elif la1 and la1 in [IDENT,DOT]:
                pass
                c2=self.tgtSimpleConfig(_t)
                _t = self._retTree
                c = c + [ c2 ];
            else:
                    raise antlr.NoViableAltException(_t)
                
            _t = _t97
            _t = _t.getNextSibling()
            c = [ TGT_CONFIG ] + [[ c, "" ]];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return c
    
    def tgtListConfig(self, _t):    
        c = None
        
        tgtListConfig_AST_in = None
        if _t != antlr.ASTNULL:
            tgtListConfig_AST_in = _t
        try:      ## for error handling
            pass
            c = [];
            _t100 = _t
            tmp35_AST_in = _t
            self.match(_t,LBRACK)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==IDENT or _t.getType()==DOT):
                    pass
                    c1=self.tgtSimpleConfig(_t)
                    _t = self._retTree
                    c = c + [ c1 ];
                else:
                    break
                
            _t = _t100
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return c
    
    def tgtSimpleConfig(self, _t):    
        c = None
        
        tgtSimpleConfig_AST_in = None
        if _t != antlr.ASTNULL:
            tgtSimpleConfig_AST_in = _t
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [IDENT]:
                pass
                s=self.tgtStateReference(_t)
                _t = self._retTree
                c = [ s ];
            elif la1 and la1 in [DOT]:
                pass
                _t104 = _t
                tmp36_AST_in = _t
                self.match(_t,DOT)
                _t = _t.getFirstChild()
                s1=self.tgtSimpleConfig(_t)
                _t = self._retTree
                s2=self.tgtStateReference(_t)
                _t = self._retTree
                c = s1 + [ s2 ];
                _t = _t104
                _t = _t.getNextSibling()
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return c
    
    def tgtStateReference(self, _t):    
        s = None
        
        tgtStateReference_AST_in = None
        if _t != antlr.ASTNULL:
            tgtStateReference_AST_in = _t
        i = None
        try:      ## for error handling
            pass
            mi = []; mii = [];
            i = _t
            self.match(_t,IDENT)
            _t = _t.getNextSibling()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==LBRACK):
                    pass
                    mi=self.machineIndex(_t)
                    _t = self._retTree
                else:
                    break
                
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [COLON]:
                pass
                mii=self.machineInstanceIdentifier(_t)
                _t = self._retTree
            elif la1 and la1 in [3,IDENT,DOT]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            s = [ i.getText(), mi, mii ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return s
    
    def machineIndex(self, _t):    
        i = None
        
        machineIndex_AST_in = None
        if _t != antlr.ASTNULL:
            machineIndex_AST_in = _t
        try:      ## for error handling
            pass
            setget = GET_INDEX;
            _t115 = _t
            tmp37_AST_in = _t
            self.match(_t,LBRACK)
            _t = _t.getFirstChild()
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [EXPR,QUESTION]:
                pass
                if not _t:
                    _t = antlr.ASTNULL
                la1 = _t.getType()
                if False:
                    pass
                elif la1 and la1 in [QUESTION]:
                    pass
                    tmp38_AST_in = _t
                    self.match(_t,QUESTION)
                    _t = _t.getNextSibling()
                    setget = SET_INDEX;
                elif la1 and la1 in [EXPR]:
                    pass
                else:
                        raise antlr.NoViableAltException(_t)
                    
                pass
                e=self.expression(_t)
                _t = self._retTree
            elif la1 and la1 in [3]:
                pass
                setget = EMPTY_INDEX; e = [];
            else:
                    raise antlr.NoViableAltException(_t)
                
            i = [ setget, e ];
            _t = _t115
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return i
    
    def machineInstanceIdentifier(self, _t):    
        i = None
        
        machineInstanceIdentifier_AST_in = None
        if _t != antlr.ASTNULL:
            machineInstanceIdentifier_AST_in = _t
        try:      ## for error handling
            pass
            _t120 = _t
            tmp39_AST_in = _t
            self.match(_t,COLON)
            _t = _t.getFirstChild()
            pass
            i=self.primaryExpression(_t)
            _t = self._retTree
            _t = _t120
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return i
    
    def stateReference(self, _t):    
        s = None
        
        stateReference_AST_in = None
        if _t != antlr.ASTNULL:
            stateReference_AST_in = _t
        i = None
        try:      ## for error handling
            pass
            mi = [];
            i = _t
            self.match(_t,IDENT)
            _t = _t.getNextSibling()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==LBRACK):
                    pass
                    mi=self.machineIndex(_t)
                    _t = self._retTree
                else:
                    break
                
            s = [ i.getText(), mi ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return s
    
    def primaryExpression(self, _t):    
        pe = None
        
        primaryExpression_AST_in = None
        if _t != antlr.ASTNULL:
            primaryExpression_AST_in = _t
        id0 = None
        id1 = None
        id2 = None
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [IDENT]:
                pass
                id0 = _t
                self.match(_t,IDENT)
                _t = _t.getNextSibling()
                pe = [ id0.getText() ];
            elif la1 and la1 in [HOST_BLOCK]:
                pass
                pe=self.hostBlock(_t)
                _t = self._retTree
                pe = [ pe ];
            elif la1 and la1 in [DOT]:
                pass
                _t207 = _t
                tmp40_AST_in = _t
                self.match(_t,DOT)
                _t = _t.getFirstChild()
                pass
                pex=self.expr(_t)
                _t = self._retTree
                pe = pex;
                if not _t:
                    _t = antlr.ASTNULL
                la1 = _t.getType()
                if False:
                    pass
                elif la1 and la1 in [IDENT]:
                    pass
                    id1 = _t
                    self.match(_t,IDENT)
                    _t = _t.getNextSibling()
                    pe = pex + [ id1.getText() ];
                elif la1 and la1 in [HOST_BLOCK]:
                    pass
                    hb=self.hostBlock(_t)
                    _t = self._retTree
                    pe = pex + [ hb ];
                elif la1 and la1 in [INDEX_OP]:
                    pass
                    ai1=self.arrayIndex(_t)
                    _t = self._retTree
                    pe = pex + [ ai ];
                elif la1 and la1 in [LITERAL_new]:
                    pass
                    _t210 = _t
                    tmp41_AST_in = _t
                    self.match(_t,LITERAL_new)
                    _t = _t.getFirstChild()
                    id2 = _t
                    self.match(_t,IDENT)
                    _t = _t.getNextSibling()
                    el=self.elist(_t)
                    _t = self._retTree
                    _t = _t210
                    _t = _t.getNextSibling()
                    pe = pex + [[ NEW_EXPRESSION, id2.getText(), el ]];
                else:
                        raise antlr.NoViableAltException(_t)
                    
                _t = _t207
                _t = _t.getNextSibling()
            elif la1 and la1 in [INDEX_OP]:
                pass
                pe=self.arrayIndex(_t)
                _t = self._retTree
                pe = [ pe ];
            elif la1 and la1 in [METHOD_CALL]:
                pass
                _t211 = _t
                tmp42_AST_in = _t
                self.match(_t,METHOD_CALL)
                _t = _t.getFirstChild()
                mpe=self.primaryExpression(_t)
                _t = self._retTree
                mel=self.elist(_t)
                _t = self._retTree
                _t = _t211
                _t = _t.getNextSibling()
                pe = [[ METHOD_CALL, mpe, mel ]];
            elif la1 and la1 in [TYPECAST]:
                pass
                _t212 = _t
                tmp43_AST_in = _t
                self.match(_t,TYPECAST)
                _t = _t.getFirstChild()
                ts=self.typeSpec(_t)
                _t = self._retTree
                te=self.expr(_t)
                _t = self._retTree
                _t = _t212
                _t = _t.getNextSibling()
                pe = [[ TYPECAST, ts, te ]];
            elif la1 and la1 in [LITERAL_new]:
                pass
                pe=self.newExpression(_t)
                _t = self._retTree
                pe = [ pe ];
            elif la1 and la1 in [NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                c=self.constant(_t)
                _t = self._retTree
                pe = [ c ];
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return pe
    
    def delay(self, _t):    
        d = None
        
        delay_AST_in = None
        if _t != antlr.ASTNULL:
            delay_AST_in = _t
        d1 = None
        try:      ## for error handling
            pass
            _t132 = _t
            d1 = antlr.ifelse(_t == antlr.ASTNULL, None, _t)
            self.match(_t,LITERAL_delay)
            _t = _t.getFirstChild()
            n=self.expression(_t)
            _t = self._retTree
            _t = _t132
            _t = _t.getNextSibling()
            d = [ d1.getText(), n ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return d
    
    def hostBlock(self, _t):    
        hb = None
        
        hostBlock_AST_in = None
        if _t != antlr.ASTNULL:
            hostBlock_AST_in = _t
        h = None
        try:      ## for error handling
            pass
            _t138 = _t
            tmp44_AST_in = _t
            self.match(_t,HOST_BLOCK)
            _t = _t.getFirstChild()
            h = _t
            self.match(_t,HOST)
            _t = _t.getNextSibling()
            _t = _t138
            _t = _t.getNextSibling()
            hb = [ HOST_BLOCK, h.getText(), AbstractMachine.getLineColumn([ h ]) ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return hb
    
    def portSend(self, _t):    
        ps = None
        
        portSend_AST_in = None
        if _t != antlr.ASTNULL:
            portSend_AST_in = _t
        try:      ## for error handling
            pass
            _t146 = _t
            tmp45_AST_in = _t
            self.match(_t,PORT_SEND)
            _t = _t.getFirstChild()
            p=self.expression(_t)
            _t = self._retTree
            m=self.expression(_t)
            _t = self._retTree
            _t = _t146
            _t = _t.getNextSibling()
            ps = [ PORT_SEND, p, m ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return ps
    
    def typeSpecArray(self, _t):    
        ta = None
        
        typeSpecArray_AST_in = None
        if _t != antlr.ASTNULL:
            typeSpecArray_AST_in = _t
        try:      ## for error handling
            pass
            ta = [];
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [ARRAY_DECLARATOR]:
                pass
                _t151 = _t
                tmp46_AST_in = _t
                self.match(_t,ARRAY_DECLARATOR)
                _t = _t.getFirstChild()
                t=self.typeSpecArray(_t)
                _t = self._retTree
                ta = ta + [ [] ] + t;
                _t = _t151
                _t = _t.getNextSibling()
            elif la1 and la1 in [IDENT,DOT]:
                pass
                pass
                i=self.identifier(_t)
                _t = self._retTree
                ta = ta + [ i ] ;
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return ta
    
    def constant(self, _t):    
        i = None
        
        constant_AST_in = None
        if _t != antlr.ASTNULL:
            constant_AST_in = _t
        i1 = None
        i2 = None
        i3 = None
        i4 = None
        i5 = None
        i6 = None
        try:      ## for error handling
            pass
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [NUM_INT]:
                pass
                i1 = _t
                self.match(_t,NUM_INT)
                _t = _t.getNextSibling()
                i = i1.getText();
            elif la1 and la1 in [CHAR_LITERAL]:
                pass
                i2 = _t
                self.match(_t,CHAR_LITERAL)
                _t = _t.getNextSibling()
                i = i2.getText();
            elif la1 and la1 in [STRING_LITERAL]:
                pass
                i3 = _t
                self.match(_t,STRING_LITERAL)
                _t = _t.getNextSibling()
                i = i3.getText();
            elif la1 and la1 in [NUM_FLOAT]:
                pass
                i4 = _t
                self.match(_t,NUM_FLOAT)
                _t = _t.getNextSibling()
                i = i4.getText();
            elif la1 and la1 in [NUM_DOUBLE]:
                pass
                i5 = _t
                self.match(_t,NUM_DOUBLE)
                _t = _t.getNextSibling()
                i = i5.getText();
            elif la1 and la1 in [NUM_LONG]:
                pass
                i6 = _t
                self.match(_t,NUM_LONG)
                _t = _t.getNextSibling()
                i = i6.getText();
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return i
    
    def expr(self, _t):    
        e = None
        
        expr_AST_in = None
        if _t != antlr.ASTNULL:
            expr_AST_in = _t
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [ASSIGN]:
                pass
                _t167 = _t
                tmp47_AST_in = _t
                self.match(_t,ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t167
                _t = _t.getNextSibling()
                e = [ ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [PLUS_ASSIGN]:
                pass
                _t168 = _t
                tmp48_AST_in = _t
                self.match(_t,PLUS_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t168
                _t = _t.getNextSibling()
                e = [ PLUS_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [MINUS_ASSIGN]:
                pass
                _t169 = _t
                tmp49_AST_in = _t
                self.match(_t,MINUS_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t169
                _t = _t.getNextSibling()
                e = [ MINUS_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [STAR_ASSIGN]:
                pass
                _t170 = _t
                tmp50_AST_in = _t
                self.match(_t,STAR_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t170
                _t = _t.getNextSibling()
                e = [ STAR_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [DIV_ASSIGN]:
                pass
                _t171 = _t
                tmp51_AST_in = _t
                self.match(_t,DIV_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t171
                _t = _t.getNextSibling()
                e = [ DIV_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [MOD_ASSIGN]:
                pass
                _t172 = _t
                tmp52_AST_in = _t
                self.match(_t,MOD_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t172
                _t = _t.getNextSibling()
                e = [ MOD_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [SR_ASSIGN]:
                pass
                _t173 = _t
                tmp53_AST_in = _t
                self.match(_t,SR_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t173
                _t = _t.getNextSibling()
                e = [ SR_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [BSR_ASSIGN]:
                pass
                _t174 = _t
                tmp54_AST_in = _t
                self.match(_t,BSR_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t174
                _t = _t.getNextSibling()
                e = [ BSR_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [SL_ASSIGN]:
                pass
                _t175 = _t
                tmp55_AST_in = _t
                self.match(_t,SL_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t175
                _t = _t.getNextSibling()
                e = [ SL_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [BAND_ASSIGN]:
                pass
                _t176 = _t
                tmp56_AST_in = _t
                self.match(_t,BAND_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t176
                _t = _t.getNextSibling()
                e = [ BAND_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [BXOR_ASSIGN]:
                pass
                _t177 = _t
                tmp57_AST_in = _t
                self.match(_t,BXOR_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t177
                _t = _t.getNextSibling()
                e = [ BXOR_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [BOR_ASSIGN]:
                pass
                _t178 = _t
                tmp58_AST_in = _t
                self.match(_t,BOR_ASSIGN)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t178
                _t = _t.getNextSibling()
                e = [ BOR_ASSIGN, ex1, ex2 ];
            elif la1 and la1 in [LOR]:
                pass
                _t179 = _t
                tmp59_AST_in = _t
                self.match(_t,LOR)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t179
                _t = _t.getNextSibling()
                e = [ LOR, ex1, ex2 ];
            elif la1 and la1 in [LAND]:
                pass
                _t180 = _t
                tmp60_AST_in = _t
                self.match(_t,LAND)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t180
                _t = _t.getNextSibling()
                e = [ LAND, ex1, ex2 ];
            elif la1 and la1 in [BOR]:
                pass
                _t181 = _t
                tmp61_AST_in = _t
                self.match(_t,BOR)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t181
                _t = _t.getNextSibling()
                e = [ BOR, ex1, ex2 ];
            elif la1 and la1 in [BXOR]:
                pass
                _t182 = _t
                tmp62_AST_in = _t
                self.match(_t,BXOR)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t182
                _t = _t.getNextSibling()
                e = [ BXOR, ex1, ex2 ];
            elif la1 and la1 in [BAND]:
                pass
                _t183 = _t
                tmp63_AST_in = _t
                self.match(_t,BAND)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t183
                _t = _t.getNextSibling()
                e = [ BAND, ex1, ex2 ];
            elif la1 and la1 in [NOT_EQUAL]:
                pass
                _t184 = _t
                tmp64_AST_in = _t
                self.match(_t,NOT_EQUAL)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t184
                _t = _t.getNextSibling()
                e = [ NOT_EQUAL, ex1, ex2 ];
            elif la1 and la1 in [EQUAL]:
                pass
                _t185 = _t
                tmp65_AST_in = _t
                self.match(_t,EQUAL)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t185
                _t = _t.getNextSibling()
                e = [ EQUAL, ex1, ex2 ];
            elif la1 and la1 in [LT]:
                pass
                _t186 = _t
                tmp66_AST_in = _t
                self.match(_t,LT)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t186
                _t = _t.getNextSibling()
                e = [ LT, ex1, ex2 ];
            elif la1 and la1 in [GT]:
                pass
                _t187 = _t
                tmp67_AST_in = _t
                self.match(_t,GT)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t187
                _t = _t.getNextSibling()
                e = [ GT, ex1, ex2 ];
            elif la1 and la1 in [LE]:
                pass
                _t188 = _t
                tmp68_AST_in = _t
                self.match(_t,LE)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t188
                _t = _t.getNextSibling()
                e = [ LE, ex1, ex2 ];
            elif la1 and la1 in [GE]:
                pass
                _t189 = _t
                tmp69_AST_in = _t
                self.match(_t,GE)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t189
                _t = _t.getNextSibling()
                e = [ GE, ex1, ex2 ];
            elif la1 and la1 in [SL]:
                pass
                _t190 = _t
                tmp70_AST_in = _t
                self.match(_t,SL)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t190
                _t = _t.getNextSibling()
                e = [ SL, ex1, ex2 ];
            elif la1 and la1 in [SR]:
                pass
                _t191 = _t
                tmp71_AST_in = _t
                self.match(_t,SR)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t191
                _t = _t.getNextSibling()
                e = [ SR, ex1, ex2 ];
            elif la1 and la1 in [BSR]:
                pass
                _t192 = _t
                tmp72_AST_in = _t
                self.match(_t,BSR)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t192
                _t = _t.getNextSibling()
                e = [ BSR, ex1, ex2 ];
            elif la1 and la1 in [PLUS]:
                pass
                _t193 = _t
                tmp73_AST_in = _t
                self.match(_t,PLUS)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t193
                _t = _t.getNextSibling()
                e = [ PLUS, ex1, ex2 ];
            elif la1 and la1 in [MINUS]:
                pass
                _t194 = _t
                tmp74_AST_in = _t
                self.match(_t,MINUS)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t194
                _t = _t.getNextSibling()
                e = [ MINUS, ex1, ex2 ];
            elif la1 and la1 in [DIV]:
                pass
                _t195 = _t
                tmp75_AST_in = _t
                self.match(_t,DIV)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t195
                _t = _t.getNextSibling()
                e = [ DIV, ex1, ex2 ];
            elif la1 and la1 in [MOD]:
                pass
                _t196 = _t
                tmp76_AST_in = _t
                self.match(_t,MOD)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t196
                _t = _t.getNextSibling()
                e = [ MOD, ex1, ex2 ];
            elif la1 and la1 in [STAR]:
                pass
                _t197 = _t
                tmp77_AST_in = _t
                self.match(_t,STAR)
                _t = _t.getFirstChild()
                ex1=self.expr(_t)
                _t = self._retTree
                ex2=self.expr(_t)
                _t = self._retTree
                _t = _t197
                _t = _t.getNextSibling()
                e = [ STAR, ex1, ex2 ];
            elif la1 and la1 in [INC]:
                pass
                _t198 = _t
                tmp78_AST_in = _t
                self.match(_t,INC)
                _t = _t.getFirstChild()
                ex=self.expr(_t)
                _t = self._retTree
                _t = _t198
                _t = _t.getNextSibling()
                e = [ INC, ex ];
            elif la1 and la1 in [DEC]:
                pass
                _t199 = _t
                tmp79_AST_in = _t
                self.match(_t,DEC)
                _t = _t.getFirstChild()
                ex=self.expr(_t)
                _t = self._retTree
                _t = _t199
                _t = _t.getNextSibling()
                e = [ DEC, ex ];
            elif la1 and la1 in [POST_INC]:
                pass
                _t200 = _t
                tmp80_AST_in = _t
                self.match(_t,POST_INC)
                _t = _t.getFirstChild()
                ex=self.expr(_t)
                _t = self._retTree
                _t = _t200
                _t = _t.getNextSibling()
                e = [ POST_INC, ex ];
            elif la1 and la1 in [POST_DEC]:
                pass
                _t201 = _t
                tmp81_AST_in = _t
                self.match(_t,POST_DEC)
                _t = _t.getFirstChild()
                ex=self.expr(_t)
                _t = self._retTree
                _t = _t201
                _t = _t.getNextSibling()
                e = [ POST_DEC, ex ];
            elif la1 and la1 in [BNOT]:
                pass
                _t202 = _t
                tmp82_AST_in = _t
                self.match(_t,BNOT)
                _t = _t.getFirstChild()
                ex=self.expr(_t)
                _t = self._retTree
                _t = _t202
                _t = _t.getNextSibling()
                e = [ BNOT, ex ];
            elif la1 and la1 in [LNOT]:
                pass
                _t203 = _t
                tmp83_AST_in = _t
                self.match(_t,LNOT)
                _t = _t.getFirstChild()
                ex=self.expr(_t)
                _t = self._retTree
                _t = _t203
                _t = _t.getNextSibling()
                e = [ LNOT, ex ];
            elif la1 and la1 in [UNARY_MINUS]:
                pass
                _t204 = _t
                tmp84_AST_in = _t
                self.match(_t,UNARY_MINUS)
                _t = _t.getFirstChild()
                ex=self.expr(_t)
                _t = self._retTree
                _t = _t204
                _t = _t.getNextSibling()
                e = [ UNARY_MINUS, ex ];
            elif la1 and la1 in [UNARY_PLUS]:
                pass
                _t205 = _t
                tmp85_AST_in = _t
                self.match(_t,UNARY_PLUS)
                _t = _t.getFirstChild()
                ex=self.expr(_t)
                _t = self._retTree
                _t = _t205
                _t = _t.getNextSibling()
                e = [ UNARY_PLUS, ex ];
            elif la1 and la1 in [HOST_BLOCK,METHOD_CALL,INDEX_OP,TYPECAST,IDENT,DOT,LITERAL_new,NUM_INT,CHAR_LITERAL,STRING_LITERAL,NUM_FLOAT,NUM_LONG,NUM_DOUBLE]:
                pass
                e=self.primaryExpression(_t)
                _t = self._retTree
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return e
    
    def arrayIndex(self, _t):    
        ai = None
        
        arrayIndex_AST_in = None
        if _t != antlr.ASTNULL:
            arrayIndex_AST_in = _t
        try:      ## for error handling
            pass
            _t214 = _t
            tmp86_AST_in = _t
            self.match(_t,INDEX_OP)
            _t = _t.getFirstChild()
            a=self.expr(_t)
            _t = self._retTree
            i=self.expression(_t)
            _t = self._retTree
            _t = _t214
            _t = _t.getNextSibling()
            ai = [ INDEX_OP, a, i ];
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return ai
    
    def newExpression(self, _t):    
        ne = None
        
        newExpression_AST_in = None
        if _t != antlr.ASTNULL:
            newExpression_AST_in = _t
        try:      ## for error handling
            pass
            _t216 = _t
            tmp87_AST_in = _t
            self.match(_t,LITERAL_new)
            _t = _t.getFirstChild()
            t=self.identifier(_t)
            _t = self._retTree
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [ARRAY_DECLARATOR]:
                pass
                nad=self.newArrayDeclarator(_t)
                _t = self._retTree
                ne = [ NEW_EXPRESSION, t, [ ARRAY_DECLARATOR, nad ]];
                if not _t:
                    _t = antlr.ASTNULL
                la1 = _t.getType()
                if False:
                    pass
                elif la1 and la1 in [ARRAY_INIT]:
                    pass
                    ai=self.arrayInitializer(_t)
                    _t = self._retTree
                    ne = ne + [ ai ];
                elif la1 and la1 in [3]:
                    pass
                else:
                        raise antlr.NoViableAltException(_t)
                    
            elif la1 and la1 in [ELIST]:
                pass
                el=self.elist(_t)
                _t = self._retTree
                ne = [ NEW_EXPRESSION, t , el ];
            else:
                    raise antlr.NoViableAltException(_t)
                
            _t = _t216
            _t = _t.getNextSibling()
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return ne
    
    def newArrayDeclarator(self, _t):    
        nad = None
        
        newArrayDeclarator_AST_in = None
        if _t != antlr.ASTNULL:
            newArrayDeclarator_AST_in = _t
        try:      ## for error handling
            pass
            nnad = [];
            _t225 = _t
            tmp88_AST_in = _t
            self.match(_t,ARRAY_DECLARATOR)
            _t = _t.getFirstChild()
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [ARRAY_DECLARATOR]:
                pass
                nnad=self.newArrayDeclarator(_t)
                _t = self._retTree
            elif la1 and la1 in [3,EXPR]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            ex = [];
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [EXPR]:
                pass
                ex=self.expression(_t)
                _t = self._retTree
            elif la1 and la1 in [3]:
                pass
            else:
                    raise antlr.NoViableAltException(_t)
                
            _t = _t225
            _t = _t.getNextSibling()
            nad = nnad + [ ex ] ;
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return nad
    
    def arrayInitializer(self, _t):    
        ai = None
        
        arrayInitializer_AST_in = None
        if _t != antlr.ASTNULL:
            arrayInitializer_AST_in = _t
        try:      ## for error handling
            pass
            ai = [];
            _t221 = _t
            tmp89_AST_in = _t
            self.match(_t,ARRAY_INIT)
            _t = _t.getFirstChild()
            while True:
                if not _t:
                    _t = antlr.ASTNULL
                if (_t.getType()==EXPR or _t.getType()==ARRAY_INIT):
                    pass
                    i=self.initializer(_t)
                    _t = self._retTree
                    ai = ai + [ i ];
                else:
                    break
                
            _t = _t221
            _t = _t.getNextSibling()
            ai = [ ARRAY_INIT ] + ai;
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return ai
    
    def initializer(self, _t):    
        init = None
        
        initializer_AST_in = None
        if _t != antlr.ASTNULL:
            initializer_AST_in = _t
        try:      ## for error handling
            if not _t:
                _t = antlr.ASTNULL
            la1 = _t.getType()
            if False:
                pass
            elif la1 and la1 in [EXPR]:
                pass
                init=self.expression(_t)
                _t = self._retTree
            elif la1 and la1 in [ARRAY_INIT]:
                pass
                init=self.arrayInitializer(_t)
                _t = self._retTree
            else:
                    raise antlr.NoViableAltException(_t)
                
        
        except antlr.RecognitionException, ex:
            self.reportError(ex)
            if _t:
                _t = _t.getNextSibling()
        
        self._retTree = _t
        return init
    

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
    
