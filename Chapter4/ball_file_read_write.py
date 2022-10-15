def read_ball_file(filename):
    infile=open(filename,'r')
    v_line=infile.readline()
    v0=float(v_line.split()[1])
    t=[]
    infile.readline()
    for line in infile:
        num=line.split()
        for n in num:
            t.append(float(n))
    infile.close()
    return t,v0

def test_read_write_file():
    v0=2.0;a=0;h=0.005
    t=[a+(i*h) for i in range(32)]
    filename='test_ball.dat'
    outfile=open(filename,'w')
    outfile.write('v: %f\n'%v0)
    outfile.write('t:\n')
    for i in range(len(t)):
        outfile.write('%g '%t[i])
        if i%6==0:
            outfile.write('\n')
    outfile.close()
    t_read,v_read=read_ball_file(filename)
    success_t=(t_read==t)
    success_v=abs(v_read-v0)<1e-5
    msg_t='The read values for t do not match the values written'
    msg_v='The read value for v does not match the value written'
    assert success_t,msg_t
    assert success_v,msg_v

def calc_write_y(filename):
    t,v0=read_ball_file(filename)
    g=9.81
    y=[v0*tt-0.5*g*tt**2 for tt in t]
    t.sort()
    y.sort()
    filename_y='ball_displacement.dat'
    outfile=open(filename_y,'w')
    outfile.write('{:<15} {:<15}'.format("t","y(t)"))
    outfile.write('\n')
    for i in range(len(t)):
        outfile.write('{:<15} {:<15}'.format(t[i],y[i]))
        outfile.write('\n')
    outfile.close()

test_read_write_file()
filename='ball.dat'
calc_write_y(filename)



