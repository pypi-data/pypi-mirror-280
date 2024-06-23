# Try to approximate squared-exponential kernel:
using PyPlot
using Optim

function gaussian_approx()

ntime = 1000
time = collect(linspace(0,10,ntime))
gaussian=exp(-time.^2/2.)

function compute_chi(x)
model = zeros(ntime)
for k=1:nexp
  model += x[1+(k-1)*3].*exp(-x[2+(k-1)*3].*time).*cos(x[3+(k-1)*3].*time)
end
return sum((gaussian-model).^2)
end  

nexp = 3
#nexp = 2
#nexp = 4
npar = 3*nexp
abest=zeros(npar)
#abest[1:12]=[1./6.,0.1,sqrt(3.),1./6.,0.1,sqrt(5.),1./3.,0.1,0.1,1./3.,0.1,0.2]
# Here are best parameters so far:
#New minimum: 855 2.522483789529161 [0.09778291672462784,1.5548632770098678,0.32192744041675075,0.596959899332403,0.3132368383113517,-0.18163977156887445,0.2670528045472698,-1.075894228060323]
#abest=[0.09778291672462784,1.5548632770098678,0.32192744041675075,0.596959899332403,0.3132368383113517,-0.18163977156887445,0.2670528045472698,-1.075894228060323]
#New minimum: 4.2559231434310284e-7 [1.4707280328402002,1.3556988707754538,1.9133776307579318,-0.7331091089111925,3.6344847969483203,1.3207054708438177,-2.5676669507901395,1.4654679150660068,-1.8772555559415482,2.8301497749105042,1.5683246010038931,0.32031045862921226] 2.0325193117951805e-5
#abest=[1.4707280328402002,1.3556988707754538,1.9133776307579318,-0.7331091089111925,3.6344847969483203,1.3207054708438177,-2.5676669507901395,1.4654679150660068,-1.8772555559415482,2.8301497749105042,1.5683246010038931,0.32031045862921226]
#New minimum: 6.819157755054511e-6 [2.7518074963750734,1.5312499407621147,-0.34148888178746056,-0.3546256365636662,4.753504292338284,2.042571639590954,-1.3968344706386124,1.7967431129812566,-1.7641684073510928] 8.113071479846436e-5 0.00034738917279475423
abest=[2.7518074963750734,1.5312499407621147,-0.34148888178746056,-0.3546256365636662,4.753504292338284,2.042571639590954,-1.3968344706386124,1.7967431129812566,-1.7641684073510928]
#abest=[2.7518074963750734,1.5312499407621147,-0.34148888178746056,-0.3546256365636662,4.753504292338284,2.042571639590954]


atrial = zeros(npar)
for k=1:npar
  atrial[k] = abest[k]
end
model = zeros(ntime)
for k=1:nexp
  model += atrial[1+(k-1)*3].*exp(-atrial[2+(k-1)*3].*time).*cos(atrial[3+(k-1)*3].*time)
end
clf()
plot(time,gaussian)
plot(time,model)
#chibest=sum((gaussian-model).^2)
chibest=compute_chi(atrial)

println("Initial chi-square: ",chibest)
read(STDIN,Char)

result = optimize(compute_chi, atrial, BFGS(), OptimizationOptions(autodiff = true))

println(Optim.minimizer(result),Optim.minimum(result))
abest= Optim.minimizer(result)
clf()
plot(time,gaussian)
plot(time,model)
model = zeros(ntime)
for k=1:nexp
  model += abest[1+(k-1)*3].*exp(-abest[2+(k-1)*3].*time).*cos(abest[3+(k-1)*3].*time)
end
plot(time,(gaussian-model))
chi=sum((gaussian-model).^2)
println("New minimum: ",chi," ",abest," ",std(gaussian-model)," ",maximum(abs(gaussian-model)))
read(STDIN,Char)

time2 = collect(linspace(0,100,ntime))
gaussian2=exp(-time2.^2/2.)
model2 = zeros(ntime)
for k=1:nexp
  model2 += abest[1+(k-1)*3].*exp(-abest[2+(k-1)*3].*time2).*cos(abest[3+(k-1)*3].*time2)
end
plot(time2,gaussian2)
plot(time2,model2)
plot(time2,gaussian2-model2)
chi2=sum((gaussian2-model2).^2)
println("New minimum: ",chi2," ",abest," ",std(gaussian2-model2)," ",maximum(abs(gaussian2-model2)))

end
