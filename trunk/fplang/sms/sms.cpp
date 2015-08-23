#include "libfetion/libfetion.h"
#include <boost/python.hpp>
#include <boost/foreach.hpp>
#include <string>
using std::string;
using namespace boost;
using namespace boost::python;
#define foreach BOOST_FOREACH
using namespace std;
BOOST_PYTHON_MODULE(sms)
{
    fx_init();
	def("login",fs_login);
	def("send",fs_send_sms_by_mobile_no);
}
