fig, ax1 = plt.subplots()

ax1.plot(D/1.8897,power_law_1,linewidth=3,color='red',label=r'$CNT + NH_3\;(PBE-vdW-dZK)$')
ax1.plot(D/1.8897,power_law_2,linewidth=3,linestyle='dashed',color='green',label=r'$CNT + NH_3\;(SCAN-vdW-dZK)$')
ax1.set_xlabel('Adsorption Distance (D/Angstrom)',fontsize=18)
ax1.set_ylabel(r'$Power\;Law,\;P(D)$',fontsize=18)
#plt.xlim(0, 10)
plt.ylim(-5, 2)
ax1.legend(fontsize=18)
plt.rc('xtick',labelsize=22)
plt.rc('ytick',labelsize=22)

# Create a set of inset Axes: these should fill the bounding box allocated to them.
ax2 = plt.axes([0,0,1,1])

# Manually set the position and relative size of the inset axes within ax1
#The list of values [0.4,0.2,0.5,0.5] set the lower left position of the Axes (x, y coordinates) and its width and height respectively in fractional units of the dimensions of the enclosing Axes, ax1. That is, for example, the height of the inset Axes are half of the height of the outer Axes.
ip = InsetPosition(ax1, [0.5,0.3,0.4,0.4])
ax2.set_axes_locator(ip)
# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
#Finally, mark_inset is used to draw a box around the region of ax1 corresponding to the data plotted in the inset, ax2. Lines are drawn between corresponding corners of the Axes indicated by loc1 and loc2: here, 2 and 4 are the "top left" and "bottom right" corners.
mark_inset(ax1, ax2, loc1=3, loc2=4, fc="none", ec='0.5')

ax2.plot(D/1.8897,power_law_1,linewidth=3,color='red')
ax2.plot(D/1.8897,power_law_2,linewidth=3,linestyle='dashed',color='green')
plt.xlim(0, 1)
plt.ylim(-5, 2)
ax2.set_xticks(np.arange(0,1.2,0.2))
ax2.set_yticks(np.arange(-5,2))
ax2.set_xlabel('Adsorption Distance (D/Angstrom)',fontsize=14)
ax2.set_ylabel(r'$Power\;Law,\;P(D)$',fontsize=14)
plt.show()
