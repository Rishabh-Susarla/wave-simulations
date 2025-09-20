# wave-simulations
A collection of wave simulations that show concepts such as beat phenomenon, the doppler effect, and wave interference. 

- Beat phenomenon: Displays how two superimposed waves with similar wavelengths can create a superposed wave and an envelope, which can be used in contexts explaining group and phase velocity (This simulation in particular displays a dispersive medium, in which the group velocity is indeed not the same as the phase velocity, which can be seen by the superposed wave not traveling at the same speed as the envelope wave). Made inspired by MIT OpenCourseWare 8.03!!
- Doppler effect: Displays the wavefronts occurring as a point source moves. This shows the doppler effect, as the percieved frequency of waves appears higher in the direction of motion of the point source, and vice versa in the direction opposite to its motion, as well as mach cones when the velocity of the point source is greater than the speed of wave propagation.

Both run with Python 3.11+, with matplotlib and numpy installed.
<table>
  <tr>
  <td> <img src = "https://github.com/user-attachments/assets/bec5b776-f230-4dfb-b76b-56bebd83c496" /> </td>
  </tr>
</table>
<sub> (The superposed wave, in blue, with the envelope wave, in green; notice how the envelope travels faster relative to the superposed wave. To observe v_p > v_g, set alpha to a negative value with magnitude less than 1/k^2.) </sub>
<br>
<table>
  <tr>
    <br>
    <td> <img src = "https://github.com/user-attachments/assets/b2e45b96-a42b-44c5-a12d-a99b81d544ec" /> </td>
  </tr>
</table>
<sub> (Visual of wavefronts traveling behind a point source. To see a better example of the doppler effect, set the velocity of the wavefront propagation to slightly less than that of the point source.) </sub>


