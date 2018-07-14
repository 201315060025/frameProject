#coding:utf-8

from handlers.index import IndexHandler
from handlers.register import RegisterHandler
from handlers.login import LoginHandler, LogOut
from handlers.updateuser import UpdateUserHandler
from handlers.applyjoinActHandler import ApplyJoinActHandler
from handlers.applyjoinOrgHandler import ApplyJoinOrgHandler
from handlers.approveCreateAct import ApproveCreateActHandler
from handlers.approveCreateOrg import ApproveCreateOrgHandler
from handlers.attendUserHandler import AttendUserHandler
from handlers.createactHandler import CreateActHandler
from handlers.createorgHandler import CreateOrgHandler
from handlers.pullActDetailsHandler import PullActDetailsHandler
from handlers.pullAllIDHandler import PullAllOrgHandler
from handlers.pullApplyCreateActDetailsHandler import PullApplyCreateActDetailsHandler
from handlers.pullApplyCreateOrgDetailsHandler import PullApplyCreateOrgDetailsHandler
from handlers.pullOrgDetailsHandler import PullOrgDetailsHandler
from handlers.pullStuDetailsHandler import PullStuDetailsHandler
from handlers.updateActHandler import UpdateActHandler
from handlers.updateOrgHandler import UpdateOrgHandler
from handlers.approveJoinOrg import ApproveJoinOrgHandler
from handlers.approveJoinAct import ApproveJoinActHandler
from handlers.pullapplyjoinActHandler import PullApplyJoinActHanler
from handlers.pullapplyjoinOrgHandler import PullApplyJoinOrgHanler
from handlers.fileHandler3 import FileHandler1
from handlers.getCode import GetCodeHandler
from handlers.queryaEarthquake import QuearEarthquakeHandler, QuearUserHandler
from handlers.editInfo import EditEarthquakeInfo, EditUserInfo
from handlers.saveInfo import SaveEarthquakeInfo,SaveUserInfo
from handlers.earthIndex import GetEartquakeInfo,GetMapInfo


urls = [
(r"/index", IndexHandler),
(r"/register", RegisterHandler),
(r"/login", LoginHandler),
(r"/updateuser", UpdateUserHandler),
(r"/createact", CreateActHandler),
(r"/createorg", CreateOrgHandler),
(r"/createactHandler", CreateActHandler),
(r"/joinorg", ApplyJoinOrgHandler),
(r"/joinact", ApplyJoinActHandler),
(r"/updateorg", UpdateOrgHandler),
(r"/updateact", UpdateActHandler),
(r"/pullorgdetail", PullOrgDetailsHandler),
(r"/pullactdetail", PullActDetailsHandler),
(r"/pulluserdetail", PullStuDetailsHandler),
(r"/pullcreateorgdetail", PullApplyCreateOrgDetailsHandler),
(r"/pullcreateactdetail", PullApplyCreateActDetailsHandler),
(r"/pullapplyjoinact", PullApplyJoinActHanler),
(r"/pullapplyjoinorg", PullApplyJoinOrgHanler),

(r"/attenduser", AttendUserHandler),
(r"/approveorg", ApproveCreateOrgHandler),
(r"/approveact", ApproveCreateActHandler),
(r"/approvejoinorg", ApproveJoinOrgHandler),
(r"/approvejoinact", ApproveJoinActHandler),
(r"/pullallorg", PullAllOrgHandler),
(r"/filehandle", FileHandler1),

(r"/getcode/(\d*)", GetCodeHandler),

(r"/queryearthquake", QuearEarthquakeHandler),
(r"/queryuserinfo", QuearUserHandler),

(r"/editearthquakeinfo", EditEarthquakeInfo),

(r"/edituserinfo", EditUserInfo),

(r"/saveearthquakeinfo", SaveEarthquakeInfo),
(r"/saveuserinfo", SaveUserInfo),
(r"/logout", LogOut),

(r"/getmapinfo", GetMapInfo),
(r"/getearthquakeinfo", GetEartquakeInfo),

]