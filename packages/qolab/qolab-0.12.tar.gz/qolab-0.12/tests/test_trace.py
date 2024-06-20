from qolab.data.trace import loadTrace
import numpy as np

def test_load_uncompressed_v0dot1_trace():
    tr = loadTrace('tests/trace_test_data/xtrace1.dat')
    cfg = tr.getConfig()
    assert cfg['config']['version'] == '0.1'
    assert cfg['config']['model'] == 'Trace'
    data = tr.getData()
    assert np.all( (data - np.array([[1], [3], [2], [5]])) == 0 )

def test_load_gzip_compressed_v0dot1_trace():
    tr = loadTrace('tests/trace_test_data/xtrace1.dat.gz')
    cfg = tr.getConfig()
    assert cfg['config']['version'] == '0.1'
    assert cfg['config']['model'] == 'Trace'
    data = tr.getData()
    assert np.all( (data - np.array([[1], [3], [2], [5]])) == 0 )

