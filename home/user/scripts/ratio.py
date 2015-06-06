#!/usr/bin/python
#
#
# DO WHATEVER YOU WANT WITH THIS (to the public domain) [mixed between the WTFPL and MIT licenses].
#
# Everyone is permitted to copy, distribute verbatim or modified copies of this software, and
# changing it as long as the name is changed.
#
# THIS SOFTWARE IS LIKE IT IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# COPYING, DISTRIBUTION AND MODIFICATION ARE ALLOWED.
#
# Just do whatever you want until the name is changed if any modification are being done.
#
#
# Copyright "(C)" 2015 NyanKiyoshi - https://github.com/NyanKiyoshi/
#
#
# Usage Example (as __main__):
#   Original Width [required]: 1200
#   Original Height [required]: 600
#   New Width [optional]:
#   Nothing given, continuing...
#   New Height [optional]: 500
#       Old Ratio : 2.0
#       New Ratio : 1.66666666667
#
#       New Height: 600
#       New Width : 1000.0
#
from __future__ import division
from sys import version_info


def main(original_width, original_height, new_width=0, new_height=0):
    width = (new_height * original_width / original_height) if new_height else original_width
    height = (original_height * new_width / original_width) if new_width else original_height
    return {'old_ratio': original_width/original_height, 'new_ratio': width/height, 'height': height, 'width': width}


if __name__ == '__main__':
    def ask(answer, required=True):
        # while -1 <= `w1` >= 1
        ans = 0
        while 1:
            try:
                ans = _input(answer + ' [%s]: ' % ['optional', 'required'][required]).strip()
                if not ans and not required:
                    print('Nothing given, continuing...')
                    break
                ans = int(ans)
                if ans:
                    break
                print('Range Error: must be less or greater than 0.')
            except ValueError:
                print('Invalid type: must be a number.')
        return ans

    r = {'original_width': 0, 'original_height': 0, 'new_width': 0, 'new_height': 0}
    # Python3.x -> _input = input
    # Python2.x -> _input = raw_input
    _input = raw_input if version_info.major == 2 else input

    i = 0
    for k in ['original_width', 'original_height', 'new_width', 'new_height']:
        r[k] = ask(k.replace('_', ' ').title(), i < 2) or 0
        # if new_width is set we stop the loop
        if r[k] and i >= 2:
            break
        i += 1
    print(
        """\
    Old Ratio : %(old_ratio)s
    New Ratio : %(new_ratio)s

    New Height: %(height)s
    New Width : %(width)s""" % main(**r))
