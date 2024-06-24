from python_dxh.config import settings
from anticaptchaofficial.recaptchav3proxyless import recaptchaV3Proxyless
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask, AnticatpchaException
from anticaptchaofficial.imagecaptcha import *

class AntiCaptchaSolver:
    def __init__(self, api_key=None):
        self.api_key = api_key or settings.ANTICAPTCHA_API_KEY
        self.solver = recaptchaV3Proxyless()
        self.solver.set_verbose(1)
        self.solver.set_key(self.api_key)
    
    def solve_recaptcha_v3(self, url, site_key, min_score=0.3, soft_id=0):
        '''
        This method is used to solve recaptcha v3 using AntiCaptcha API
        '''
        self.solver.set_website_url(url)
        self.solver.set_website_key(site_key)
        self.solver.set_min_score(min_score)
        self.solver.set_soft_id(soft_id)
        g_response = self.solver.solve_and_return_solution()
        return g_response 
    

    def solve_recaptcha_v2(self, url, site_key):
        '''
        This method is used to solve recaptcha v2 (invisible) using AntiCaptcha API
        '''
        client = AnticaptchaClient(self.api_key)
        task = NoCaptchaTaskProxylessTask(url, site_key, is_invisible=True)
        job = client.createTask(task)
        try:
            job.join(maximum_time=15)  # Set the maximum_time value in seconds
        except AnticatpchaException as e:
            return None
        
        g_response = job.get_solution_response()
        return g_response
    
    def solve_image_captcha(self, captcha_filename):
        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key(self.api_key)
        solver.set_soft_id(0)
        captcha_text = solver.solve_and_return_solution(captcha_filename)
        return captcha_text
    



# Usage Example:
# solver = AntiCaptchaSolver()
# g_response = solver.solve_recaptcha_v3('http://example.com', 'site-key')
# print(g_response)
# g_response = solver.solve_recaptcha_v2('http://example.com', 'site-key')
# print(g_response)
# captcha_text = solver.solve_image_captcha('captcha.png')
# print(captcha_text)