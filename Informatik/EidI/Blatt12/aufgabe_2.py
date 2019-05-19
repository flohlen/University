from jobinterface import Job, JobException, TryAgainLaterException
import random

#
# signalisiert einen Underflow des Scheduler - nicht veraendern
# 
class SchedulerUnderflowException(Exception): 
	pass

class Scheduler(object):


	def __init__(self): # nicht veraendern
		self.schlange = []
		self.log = []

	def neuerjob(self, job): #zu implementieren
		assert isinstance(job, Job) == True, "Job ist kein Job."
		self.schlange.append(job)
		return job


	def laufe(self, wieviele): # uzu implementieren

		ret_vals = []

		assert type(wieviele) == int and wieviele > 0, "Wie viele ist kein int oder nicht groesser als 0."

		try:

			for x in range(wieviele):
				if len(self.schlange) == 0:
					raise SchedulerUnderflowException
				
				jbb = self.schlange.pop(0)

				try:

					jbb_val = jbb.start()

					assert type(jbb_val) == int and jbb_val > 0, "Der Rueckgabewert ist kein int oder nicht positiv."

					ret_vals.append(jbb_val)
					self.log.append("LOG: Job " + str(jbb.get_id()) + " wurde erfolgreich ausgefuehrt.")

				except TryAgainLaterException:

					self.schlange.append(jbb)
					self.log.append("LOG: Job " + str(jbb.get_id()) + " konnte nicht ausgefuehrt werden und wurde erneut zur Schlange hinzugefuegt.")	
				
				except:

					self.log.append("LOG: Job " + str(jbb.get_id()) + " konnte nicht ausgefuehrt werden und wurde entfernt.")
					assert type(jbb_val) == int and jbb_val > 0, "Der Rueckgabewert ist kein int oder nicht positiv." 


		except SchedulerUnderflowException:
			ret_vals = []

		else:
			assert False, "d test"

		finally:
			return ret_vals


if __name__ == '__main__':

#
# Loesen Sie Aufgabenteil c) hier:
#

	class BadTestException(JobException):
		pass

	class JBE1(Job):

		def __init__(self):
			super().__init__()
			self.run = False

		def start(self):
			if self.run:
				return random.randint(1,10)
			else:
				self.run = True
				raise TryAgainLaterException

	class JBE2(Job):

		def start(self):
			return random.randint(1,10)

	class JBE3(Job):
		
		def start(self):
			return instance(BadTestException)

	class JBE4(Job):

		def start(self):
			return "beeb boob"


#
# Loesen Sie Aufgabenteil d) hier:
#

	test = Scheduler()

	job_1 = JBE1()
	job_2 = JBE2()
	job_3 = JBE3()
	job_4 = JBE4()

	test.neuerjob(job_1)
	test.neuerjob(job_2)
	test.neuerjob(job_3)

	# d) - 1

	vals = test.laufe(4)

	assert len(test.schlange) == 0, "Schlange ist nicht leer." 

	for x in vals:
		assert type(x) == int and x > 0, "Werte sind kein int oder nicht groesser als 0."

	print(test.log) # Logbuch: Job 0 nicht erfolgreich und erneut in schlange, Job 1 erfolgreich, Job 2 nicht erfolgreich und entfernt, Job 0 erfolgreich #

	# d) - 2

	test.neuerjob(job_1)
	test.neuerjob(job_2)
	test.neuerjob(job_3)

	vals = test.laufe(5)
	assert len(vals) == 0, "Rueckgabewerte sind nicht leer"

	# es gibt keinen AssertionError mit "d Test"
	
	# d) - 3
	test.neuerjob(job_4)

	vals = test.laufe(1)

	# d) - 4
	test.neuerjob(BadTestException)
	test.laufe(1.5)
	test.laufe(-1)

	test.laufe(1)

# Ihren globalen Testcode koennen Sie hier platzieren: