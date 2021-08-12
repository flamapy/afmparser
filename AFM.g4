grammar AFM;

//parser rules

//model
feature_model: relationships_block;

//relationships block

relationships_block: '%Relationships' relationship_spec*;

relationship_spec:
	init_spec (non_cardinal_spec | cardinal_spec) ';';

init_spec: SPACE? FEATURE SPACE? ':' SPACE?;

obligatory_spec: SPACE? FEATURE SPACE?;
optional_spec: SPACE? '[' FEATURE ']' SPACE?;

non_cardinal_spec: (obligatory_spec | optional_spec)+;

cardinality: '[' INT ',' INT ']';
cardinal_spec:
	SPACE? cardinality SPACE? '{' obligatory_spec+ '}';

//lexer rules

FEATURE: [A-Z][a-zA-Z]*;
INT: [1-9][0-9]*;

SPACE: (' ' | '\t')+;
WS: [\n\r]+ -> skip;