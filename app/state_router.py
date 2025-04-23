from app.states import Status
from app.handlers import main_menu
from app.training import study_0, study_1
from app.on_site_medical_aid import help_on_place_0
from app.emergency_services import emergency_0, emergency_2
from app.about import about_0



state_handlers = {
    Status.esha0.state: main_menu,
    Status.e1e3.state: emergency_0,
    Status.h1h8.state: help_on_place_0,
    Status.s1s4.state: study_0,
    Status.s11_s15.state: study_1,
    Status.a1_a2: about_0,
    Status.e11_e19: emergency_2
}

