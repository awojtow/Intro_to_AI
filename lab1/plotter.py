from methods import Method
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
def plot_method(mlist: list, ncol: int, nrow:int, name: str = 'subplot', method: str = 'method', minimum:tuple = (1,1)):
        fig, axes = plt.subplots(nrow,ncol, figsize = [8,8])
        x_st = np.linspace(-6, 6, 100)
        y_st = np.linspace(-6, 6, 100)
        X_st, Y_st = np.meshgrid(x_st, y_st)
        for c in range(ncol):
            for r in range(nrow): 
                m = mlist[(ncol+1)*c+r]
                x_pos = [p[0] for p in m.pos]
                y_pos = [p[1] for p in m.pos]
                
                x = np.linspace(min(-5.2,min(x_pos)+0.2), max(5.2,max(x_pos)+0.2), 200)
                y = np.linspace(min(-5.2,min(y_pos)+0.2), max(5.2,max(y_pos)+0.2), 200)
                X, Y = np.meshgrid(x, y)
                Z = m.fun.fun(X, Y)
                Z_st = m.fun.fun(X_st, Y_st)
                
                
                ax = axes[r,c]
                pcm = ax.pcolor(X, Y, Z,
                   norm=colors.LogNorm(vmin=Z_st.min(), vmax=Z_st.max()),
                cmap='magma', shading='auto')
                
                ax.hlines(y=-5, xmin=-5, xmax=5, linewidth=3, color='white')
                ax.hlines(y=5, xmin=-5, xmax=5, linewidth=3, color='white')
                ax.vlines(x=-5, ymin=-5, ymax=5, linewidth=3, color='white')
                ax.vlines(x=5, ymin=-5, ymax=5, linewidth=3, color='white')
                
                ax.plot(x_pos, y_pos, 'lime', linewidth = 0.3)
                ax.plot(x_pos, y_pos, 'g.', markersize = 3)
                ax.plot(x_pos[0], y_pos[0], 'yo', markersize = 5)
                ax.plot(x_pos[-1], y_pos[-1], 'y*', markersize = 5)
                ax.plot(minimum[0],minimum[1],'c*', markersize = 5)
                
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_title(f"beta = {m.beta} \nstart = {m.init_point}, end = [{round(m.pos[-1][0],3)},{round(m.pos[-1][1],3)}] \ndone iter {m.done_iter}/{m.max_iter}", size = 7) 
        plt.tight_layout()
        fig.subplots_adjust(right=0.825)
        cax = fig.add_axes([0.85, 0.06, 0.035, 0.91])
        fig.colorbar(pcm, cax=cax)
        plt.suptitle(method)
        plt.savefig(name)
