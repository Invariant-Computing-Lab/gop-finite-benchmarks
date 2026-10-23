import json
from pathlib import Path
import omega_gop as g
functions = ['g1_gauge', 'g2_inverse_square', 'g3_quintic_stochastic', 'g4_s05', 'g5_s07', 'g6_quantum_learned', 'g7_memory']
if __name__ == '__main__':
    result=[getattr(g,n)() for n in functions]
    Path('replay_result.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({'executed':len(result),'status':'FINITE_REPLAY_NEGATIVES_RETAINED'}))
