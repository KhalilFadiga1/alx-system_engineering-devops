#!/usr/bin/pup
#Install a specific a version of flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip'
}
