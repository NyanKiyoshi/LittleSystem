# LittleSystem
Miscellaneous scripts, customizations, settings, etc. For Linux users (often written on Arch).


Table
=====
#### System Script
- [/etc/profile.d/startup.sh](/etc/profile.d/startup.sh)

    Loads the X11 environment from the ~/.xinitrc when the user login into the TTY1 and if a X environment is not already started.
- [/etc/init.d/transmission-daemon](/etc/init.d/transmission-daemon)

    Modified service file for the transmission's daemon with support of logging (written under Debian).

#### User Script/ User Customizations
- [/home/user/scripts/ratio.py](/home/user/scripts/ratio.py)

    Calculates the ratio aspect from a given height and width and if given, from the new height or new width.

- [/home/user/.Xresources](/home/user/.Xresources)

    Customizations for [URXVT](http://software.schmorp.de/pkg/rxvt-unicode). [[Preview](https://i.imgur.com/95T3Gn9.png)]


License
=======
```
DO WHATEVER YOU WANT WITH THIS (to the public domain) [mixed between the WTFPL and MIT licenses].

Everyone is permitted to copy, distribute verbatim or modified copies of this software, and
changing it as long as the name is changed.

THIS SOFTWARE IS LIKE IT IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

COPYING, DISTRIBUTION AND MODIFICATION ARE ALLOWED.

Just do whatever you want until the name is changed if any modification are being done.


Copyright "(C)" 2015 NyanKiyoshi - https://github.com/NyanKiyoshi/
```
