import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def bezier_curve(control_points, t):
    """
    Calculate a Bézier curve point and intermediate points using the De Casteljau algorithm.
    """
    def de_casteljau_with_steps(points, t):
        if len(points) == 1:
            return [points]
        new_points = [
            ((1 - t) * p0[0] + t * p1[0], (1 - t) * p0[1] + t * p1[1])
            for p0, p1 in zip(points[:-1], points[1:])
        ]
        return [points] + de_casteljau_with_steps(new_points, t)

    all_steps = de_casteljau_with_steps(control_points, t)
    return all_steps

def animate_bezier():
    # Define control points
    control_points = [(0, 0), (1, 2), (3, 3), (4, 0)]
    
    # Create storage for curve points
    curve_points = []
    
    # Setup the figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 3.5)
    
    # Plot control points
    control_x, control_y = zip(*control_points)
    ax.plot(control_x, control_y, 'o--', color='red', label='Control Points')
    
    # Create line objects
    curve_line, = ax.plot([], [], 'b-', label='Bézier Curve')
    intermediate_lines = []
    intermediate_points = []
    
    # Colors for intermediate steps
    colors = ['gray', 'lightgray', 'darkgray']
    
    # Initialize intermediate lines and points
    for i in range(len(control_points) - 1):
        line, = ax.plot([], [], 'o-', color=colors[i % len(colors)])
        intermediate_lines.append(line)
        point, = ax.plot([], [], 'o', color=colors[i % len(colors)])
        intermediate_points.append(point)
    
    def init():
        curve_line.set_data([], [])
        for line in intermediate_lines:
            line.set_data([], [])
        for point in intermediate_points:
            point.set_data([], [])
        return [curve_line] + intermediate_lines + intermediate_points
    
    def update(frame):
        t = frame / 100
        
        # Calculate all points for current t
        all_steps = bezier_curve(control_points, t)
        
        # Update intermediate lines and points
        for i, points in enumerate(all_steps[1:]):
            x_vals, y_vals = zip(*points)
            intermediate_lines[i].set_data(x_vals, y_vals)
            intermediate_points[i].set_data(x_vals, y_vals)
        
        # Get the current point on the curve
        current_point = all_steps[-1][0]
        curve_points.append(current_point)
        
        # Update the curve with all points so far
        if curve_points:
            curve_x, curve_y = zip(*curve_points)
            curve_line.set_data(curve_x, curve_y)
        
        return [curve_line] + intermediate_lines + intermediate_points
    
    # Create animation
    anim = FuncAnimation(fig, update, frames=101, init_func=init, interval=50, blit=True)
    
    # Add title and labels
    plt.title("Bézier Curve Construction Animation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    
    # Save as GIF
    writer = PillowWriter(fps=20)
    anim.save('bezier_animation.gif', writer=writer)
    plt.close()

if __name__ == "__main__":
    animate_bezier()