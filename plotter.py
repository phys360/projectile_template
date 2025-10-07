from solver import *

def plot(x,y):

  # make a graph of the results
  fig, (ax,ax2) = plt.subplots(2,1)
  for theta in range(20, 65, 5):
    x,y = sovler(radians(theta), rho=0.5)
    ax.plot(x, y, label=r"$\theta =$" + str(theta) + "$^o$")

  ax.legend( bbox_to_anchor=(1.25, 1.0))
  ax.set_xlabel("distance [m]")
  ax.set_ylabel("height [m]")

  th = np.arange(20,60,0.5)
  max_x = []
  for theta in th:
    x,y = solver(radians(theta), rho=0.5)
    max_x.append(np.max(x))
  ax2.scatter(th, max_x)
  max_angle = th[np.argmax(max_x)]
  max_distance = np.max(max_x)
  ax2.axvline(max_angle, color='red', linestyle='--')
  ax2.text(max_angle+1, np.min(max_x)+1.5, f"max dist = {max_distance:.1f}m")
  ax2.text(max_angle+1, np.min(max_x), f"max angle = {max_angle:.2f} deg")
  ax2.set_ylabel("kick distance [m]")
  ax2.set_xlabel("kick angle [deg]")

  
  return fig