% REGLAS DE LA GRAMÁTICA

% Una oración se compone de un sintagma nominal (SN) y un sintagma verbal (SV) entonces:
o(o(SN, SV)) --> sn(SN, _Gen, Num), sv(SV, Num).

% Sintagma Nominal: requiere género y número entre determinante y nombre entonces:
sn(sn(DET, N), Gen, Num) --> det(DET, Gen, Num), n(N, Gen, Num).

% Sintagma Verbal: puede ser un verbo transitivo con objeto directo entonces:
sv(sv(VT, SN), Num) --> vt(VT, Num), sn(SN, _, _).

% o puede ser un verbo intransitivo (sin objeto).
sv(sv(VI), Num) --> vi(VI, Num).

% Determinantes 
det(det(el), m, sg) --> [el].
det(det(la), f, sg) --> [la].
det(det(los), m, pl) --> [los].
det(det(las), f, pl) --> [las].
det(det(un), m, sg) --> [un].
det(det(una), f, sg) --> [una].
det(det(unos), m, pl) --> [unos].
det(det(unas), f, pl) --> [unas].

% Nombres y sustantivos 
n(n(empleado), m, sg) --> [empleado].
n(n(empleada), f, sg) --> [empleada].
n(n(empleados), m, pl) --> [empleados].
n(n(empleadas), f, pl) --> [empleadas].
n(n(sueldo), m, sg) --> [sueldo].
n(n(sueldos), m, pl) --> [sueldos].

% Verbos intransitivos 
vi(vi(trabaja), sg) --> [trabaja].
vi(vi(trabajan), pl) --> [trabajan].

% Verbos transitivos 
vt(vt(cobra), sg) --> [cobra].
vt(vt(cobran), pl) --> [cobran].

